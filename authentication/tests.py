from django.contrib.auth.models import User
from django.test import TestCase

class LogInTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password='secret'
        User.objects.create_user(username=self.username,password=self.password)
    def test_login(self):
        response = self.client.post('/login/', {"username":self.username,"password":self.password}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

class SignInTest(TestCase):
    def setUp(self):
        self.credentials = {
        	'firstname': 'John',
        	'lastname': 'Doe',
        	'email': 'johndoe@gmail.com',
            'usernameRegister': 'testuser',
            'passwordRegister': 'secret'}
        User.objects.create_user(username=self.credentials["usernameRegister"],
        						password=self.credentials["passwordRegister"])
    def test_login(self):
        response = self.client.post('/login/', {"username":self.credentials["usernameRegister"],
        										"password":self.credentials["passwordRegister"]}, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
