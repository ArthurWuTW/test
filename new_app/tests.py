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

    def test_login(self):

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(self.live_server_url)
        print(driver.page_source)












    # TODO: test_add, test_delete, test_top3
