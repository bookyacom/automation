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
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
