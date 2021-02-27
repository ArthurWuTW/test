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

# Create your tests here.
class ViewTest(TestCase):

    def test_url_resloves_to_view(self):

        found = resolve('/')
        self.assertEqual(found.func.view_class, new_app.views.Page)

    def test_add_data(self):

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

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
        driver.get(self.live_server_url)
        print(driver.page_source)


        # Select
        opt = driver.find_element_by_name('product_name')
        Select(opt).select_by_index(1)

        # insert custom name
        driver.find_element_by_id('product_number').send_keys('5')
        driver.find_element_by_id('customer_id').send_keys('ABC')

        driver.find_element_by_id('image-btn').click()

        print(driver.page_source)
















    # TODO: test_add, test_delete, test_top3
