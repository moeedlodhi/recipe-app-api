"""Tests for models"""


from calendar import c
from django.contrib.auth import authenticate 
from django.test import TestCase
from core.models import User
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_success(self):
        """Test creating with email success"""

        email = 'test@example.com'
        password = '1234'
        user = User.objects.create(
            email = email
        )
        user.set_password(password)
        user.save()

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user is normalised"""
        sample_emails = [
            ['moeedlodhi@example.com','moeedlodhi@example.com'],
            ['TEST2@EXAMPLE.COM','TEST2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['TEST4@example.com','TEST4@example.com']
        ]  

        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email=email,password='1234')
            print(user)
            print(user.email,'****')
            self.assertEqual(user.email,expected)
    def test_new_user_without_email(self):
        """Must have email else Validation error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='',password='1234')  

    def test_create_superuser(self):
        """test creating superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='1234'
        )  
        user.username = 'test1'
        user.save()

        u = authenticate(
            email='test@example.com',
            password='1234') 
        print(u,'auth')
        print(user,"test1")   
        print(user.is_superuser)     
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


