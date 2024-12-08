from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blogapp.models import Blog


class UserAuthTests(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser', password='testpass')

    def test_register_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        # Redirección tras registro
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_user(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras login

    def test_logout_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirección tras logout
