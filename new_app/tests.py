import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
from django.test import TestCase
from django.urls import resolve
import new_app.views
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import os
from new_app.models import Product, Order

# Create your tests here.

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_insert(self):
        products = [
            [1,	6,	150,	'um',	False],
            [2,	10,	110,	'ms',	False],
            [3,	20,	900,	'ps',	False],
            [4,	2,	1899,	'ps',	True],
            [5,	8,	35,	    'ms',	False],
            [6,	5,	60,	    'um',	False],
            [7,	5,	800,	'ps',	True]
        ]

        for product in products:
            new_data = Product()
            new_data.product_id = product[0]
            new_data.stock_pcs = product[1]
            new_data.price = product[2]
            new_data.shop_id  = product[3]
            new_data.vip  = product[4]
            new_data.save()

        # check each items
        for product in products:
            queried_product = Product.objects.get(product_id=product[0])
            self.assertEqual(queried_product.stock_pcs, product[1])
            self.assertEqual(queried_product.price, product[2])
            self.assertEqual(queried_product.shop_id, product[3])
            self.assertEqual(queried_product.vip, product[4])



    def test_add(self):

        products = [
            [1,	6,	150,	'um',	False],
            [2,	10,	110,	'ms',	False],
            [3,	20,	900,	'ps',	False],
            [4,	2,	1899,	'ps',	True],
            [5,	8,	35,	    'ms',	False],
            [6,	5,	60,	    'um',	False],
            [7,	5,	800,	'ps',	True]
        ]
        from new_app.models import Product
        for product in products:
            new_data = Product()
            new_data.product_id = product[0]
            new_data.stock_pcs = product[1]
            new_data.price = product[2]
            new_data.shop_id  = product[3]
            new_data.vip  = product[4]
            new_data.save()

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        # Order every products
        for product in products:
            driver.get(self.live_server_url)

            # Select
            opt = driver.find_element_by_name('product_name')
            Select(opt).select_by_index(str(product[0]))

            # add order
            driver.find_element_by_id('product_number').send_keys(str(product[1]))
            driver.find_element_by_id('customer_id').send_keys('ABC')
            driver.find_element_by_id('isVIP').click()
            driver.find_element_by_id('image-btn').click()

            # check order
            queried_order = Order.objects.latest('id')
            self.assertEqual(queried_order.product_id, product[0])
            self.assertEqual(queried_order.qty, product[1])
            self.assertEqual(queried_order.price, product[2])
            self.assertEqual(queried_order.shop_id, product[3])
            self.assertEqual(queried_order.customer_id, 'ABC')

        driver.quit()

    def test_vip_status(self):
        products = [
            [1,	6,	150,	'um',	False],
            [2,	10,	110,	'ms',	False],
            [3,	20,	900,	'ps',	False],
            [4,	2,	1899,	'ps',	True],
            [5,	8,	35,	    'ms',	False],
            [6,	5,	60,	    'um',	False],
            [7,	5,	800,	'ps',	True]
        ]

        for product in products:
            new_data = Product()
            new_data.product_id = product[0]
            new_data.stock_pcs = product[1]
            new_data.price = product[2]
            new_data.shop_id  = product[3]
            new_data.vip  = product[4]
            new_data.save()

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        for product in products:
            if(product[4]==True):
                driver.get(self.live_server_url)
                # Select
                opt = driver.find_element_by_name('product_name')
                Select(opt).select_by_index(str(product[0]))

                # add order

                driver.find_element_by_id('product_number').send_keys(str(product[1]))
                driver.find_element_by_id('customer_id').send_keys('ABC')
                driver.find_element_by_id('image-btn').click()

                self.assertIn('你不是ｖｉｐ', driver.page_source)
        driver.quit()

    def test_understock_status(self):
        products = [
            [1,	6,	150,	'um',	False],
            [2,	10,	110,	'ms',	False],
            [3,	20,	900,	'ps',	False],
            [4,	2,	1899,	'ps',	True],
            [5,	8,	35,	    'ms',	False],
            [6,	5,	60,	    'um',	False],
            [7,	5,	800,	'ps',	True]
        ]

        for product in products:
            new_data = Product()
            new_data.product_id = product[0]
            new_data.stock_pcs = product[1]
            new_data.price = product[2]
            new_data.shop_id  = product[3]
            new_data.vip  = product[4]
            new_data.save()

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        for product in products:
            if(product[4]==True):
                driver.get(self.live_server_url)
                # Select
                opt = driver.find_element_by_name('product_name')
                Select(opt).select_by_index(str(product[0]))

                # add order
                driver.find_element_by_id('product_number').send_keys(str(product[1]+1))
                driver.find_element_by_id('customer_id').send_keys('ABC')
                driver.find_element_by_id('isVIP').click()
                driver.find_element_by_id('image-btn').click()

                self.assertIn('貨源不足', driver.page_source)
        driver.quit()

    def test_stock_arrived_status(self):
        products = [
            [1,	6,	150,	'um',	False],
            [2,	10,	110,	'ms',	False],
            [3,	20,	900,	'ps',	False],
            [4,	2,	1899,	'ps',	True],
            [5,	8,	35,	    'ms',	False],
            [6,	5,	60,	    'um',	False],
            [7,	5,	800,	'ps',	True]
        ]
        from new_app.models import Product
        for product in products:
            new_data = Product()
            new_data.product_id = product[0]
            new_data.stock_pcs = product[1]
            new_data.price = product[2]
            new_data.shop_id  = product[3]
            new_data.vip  = product[4]
            new_data.save()

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        # Order every products
        for product in products:
            driver.get(self.live_server_url)

            # Select
            opt = driver.find_element_by_name('product_name')
            Select(opt).select_by_index(str(product[0]))

            # add order
            driver.find_element_by_id('product_number').send_keys(str(product[1]))
            driver.find_element_by_id('customer_id').send_keys('ABC')
            driver.find_element_by_id('isVIP').click()
            driver.find_element_by_id('image-btn').click()

            self.assertEqual(Product.objects.get(product_id=product[0]).stock_pcs, 0)

            # delete order
            queried_order = Order.objects.latest('id')
            driver.get(self.live_server_url)
            driver.find_element_by_id('image-btn-'+str(queried_order.id)).click()

            self.assertEqual(len(Order.objects.all()), 0)
        driver.quit()











    # TODO: test_add, test_delete, test_top3
