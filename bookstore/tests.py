from django.test import TestCase,SimpleTestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import Client
from .models import Book

# Create your tests here.
#test for the various routes
class ViewRoutes(TestCase):

    def test_home_page_status_code(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)


    def test_login_status_code(self):
        response=self.client.get('/login/')
        self.assertEqual(response.status_code,200)

    
    def test_signup_status_code(self):
        response=self.client.get('/register/')
        self.assertEqual(response.status_code,200)


    def test_add_book_status_code(self):
        response=self.client.get('/add_book/')
        self.assertEqual(response.status_code,200)



class BookModelTest(TestCase):
    
    def setUp(self):
        user=User.objects.create(username='jon',email='jonathan@jon.com',password='nathanoj35')
        Book.objects.create(title="Django for everyone",written=timezone.now,upload_by=user,created=timezone.now)


    def test_book_content(self):
        book=Book.objects.get(id=1)
        expected_object_name=f"{book.title}"
        self.assertEqual(expected_object_name,'Django for Every one')

