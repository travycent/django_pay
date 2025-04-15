from django.test import TestCase
from profiles.models import User

class UserManagerTest(TestCase):
    """
    Test cases for the CustomUserManager methods
    """
    def test_create_user_successful(self):
        email="inno@gmail.com"
        password="password123"
        first_name="John"
        last_name="Doe"
        
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser_successful(self):
        """
        Test that a superuser is created successfully with valid inputs.
        """
        email = "admin@example.com"
        password = "adminpassword123"

        superuser = User.objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        
    def test_create_superuser_missing_is_staff(self):
        """
        Test that creating a superuser without is_staff=True raises a ValueError.
        """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin@example.com",
                password="adminpassword123",
                is_staff=False
            )
            
    def test_create_superuser_missing_is_superuser(self):
        """
        Test that creating a superuser without is_superuser=True raises a ValueError.
        """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin@example.com",
                password="adminpassword123",
                is_superuser=False
            )
        
    
    