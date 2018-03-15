from django.urls import resolve
from django.test import TestCase
from pipelines.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
