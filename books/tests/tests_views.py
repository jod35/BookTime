from django.test import TestCase,SimpleTestCase

# Create your tests here.

#test the homepage
class HomePageTest(SimpleTestCase):
    def home_page_works_well(self):
        response=self.client.et('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/index.html')
        self.assertContains(response,'Books Time')

#test the about page
class AboutPageTest(SimpleTestCase):
    def test_homepage_work(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/about.html')

#test the contact us page

class ContactUsPageTest(TestCase):
    def test_contact_us_page_works(self):
        response=self.client.get('/contact-us/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'books/contact_form.html')
        self.assertContains(response,'BookTime')
        self.assertIsInstance(
            response.context['form'],forms.ContactForm
        )
        
