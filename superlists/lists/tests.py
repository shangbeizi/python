from django.test import TestCase
from django.core.urlresolvers import resolve
from . import views
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,views.home_page)

