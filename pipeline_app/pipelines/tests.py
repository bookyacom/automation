from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from pipelines.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>pipeline - 4 real!</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
