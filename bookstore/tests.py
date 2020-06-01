from django.test import TestCase,SimpleTestCase
from django.test import Client
# from .models import Book,Review

# Create your tests here.

class HomepageTestCase(TestCase):

    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)


    def test_login_status_code(self):
        response=self.client.get('/login/')
        self.assertEqual(response.status_code,200)

    
    def test_signup_status_code(self):
        response=self.client.get('/register/')
        self.assertEqual(response.status_code,200)

