from django.test import TestCase
from django.urls import resolve
import new_app.views
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create your tests here.
class ViewTest(TestCase):

    def test_url_resloves_to_view(self):

        found = resolve('/')
        self.assertEqual(found.func.view_class, new_app.views.Page)

    def test_add_data(self):

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        





    # TODO: test_add, test_delete, test_top3
