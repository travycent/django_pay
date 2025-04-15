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
        
    
    