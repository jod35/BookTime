from django.test import TestCase,SimpleTestCase

# Create your tests here.

class HomePageTest(SimpleTestCase):
    def home_page_works_well(self):
        response=self.client.et('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/index.html')
        self.assertContains(response,'Books Time')

    def test_homepage_work(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/about.html')