from django.test import TestCase
from django.urls import reverse
from django.http import HttpResponse

class SplashPageViewTest(TestCase):
    HTMLSTRING = """<h1>Congratulations!</h1>"""

    def test_splashpage_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)
        self.assertContains(response, self.HTMLSTRING)