from django.test import TestCase,SimpleTestCase

# Create your tests here.

class HomePageTest(SimpleTestCase):
    def home_page_works_well(self):
        response=self.client.et('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/index.html')
        self.assertContains(response,'Books Time')