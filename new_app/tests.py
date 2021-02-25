from django.test import TestCase
from django.urls import resolve
from selenium import webdriver


# Create your tests here.
class ViewTest(TestCase):

    def test_url_resloves_to_view(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, new_app.views.Page)

    # TODO: test_add, test_delete, test_top3
