from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book


from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication



class BookListViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testingUser1', password='testUserPassword1')
        self.token = TokenAuthentication.objects.create(user=self.user)
        self.client.login(username='testingUser1', password='testUserPassword1')
        self.url = reverse('book-list')
       
        self.author = Author.objects.create(name='John KK')
        self.book = Book.objects.create(
            title='Knowing the world',
            publication_year=2023,
            author= self.author
        )
    def test_book_list_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0) 

class BookDeleteViewTestCase(APITestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testingUser1', password='testUserPassword1')
            self.token = TokenAuthentication.objects.create(user=self.user)
            self.client.login(username='testingUser1', password='testUserPassword1')
        
            self.author = Author.objects.create(name='John KK')
            self.book = Book.objects.create(
                title='Knowing the world',
                publication_year=2023,
                author= self.author
            )
            self.url = reverse('book-detail', args=[self.book.id])

        def test_book_delete_view(self):
            response = self.client.delete(self.url)

            self.assertEqual(response.status_code, 204)
            self.assertEqual(Book.objects.count(), 0) 

class BookUpdateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testingUser1', password='testUserPassword1')
        self.token = TokenAuthentication.objects.create(user=self.user)
        self.client.login(username='testingUser1', password='testUserPassword1')
        
        self.author = Author.objects.create(name='John KK')
        self.book = Book.objects.create(
            title='Knowing the world',
            publication_year=2023,
            author= self.author
        )
        self.url = reverse('book-detail', args=[self.book.id])
        self.book_data = {
            'title': 'Knowing you',
            'publication_year': 2023,
            'author': self.author.id
        }

    def test_book_update_view(self):
        response = self.client.put(self.url, self.book_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get().title, 'Knowing you')
 
class BookRetrieveViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testingUser1', password='testUserPassword1')
        self.token = TokenAuthentication.objects.create(user=self.user)
        self.client.login(username='testuser', password='testpassword')

        self.author = Author.objects.create(name='George R. R. Martin')
        self.book = Book.objects.create(
            title='House of the dragon',
            publication_year=2022,
            author=self.author
        )
        self.url = reverse('book-detail', args=[self.book.id])

    def test_book_retrieve_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'House of the dragon')
        self.assertEqual(response.data['publication_year'], 2023)
        self.assertGreater(len(response.data), 0)