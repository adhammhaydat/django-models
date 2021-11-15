from django.test import TestCase
from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse


class SnacksTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("list_view")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
    
    
              