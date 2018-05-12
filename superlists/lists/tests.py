from django.test import TestCase
from django.core.urlresolvers import resolve
from . import views
from django.http import HttpRequest
from django.template.loader import render_to_string
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,views.home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = views.home_page(request)
        excepted_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),excepted_html)


