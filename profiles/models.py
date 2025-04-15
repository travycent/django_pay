from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.base_model import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Custom user model that extends AbstractBaseUser and BaseModel.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True,max_length=15,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    def get_cached_profile(self):
        """
        Get the cached profile of the user.
        """
        cache_key = f"user_profile_{self.id}"
        cached_profile = cache.get(cache_key)
        if not cached_profile:
            # Simulate fetching profile data (e.g., from related models)
            cached_profile = {
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "phone_number": self.phone_number,
            }
            # Cache the data with a timeout of 1 hour (3600 seconds)
            cache.set(cache_key, cached_profile, timeout=3600)
        return cached_profile
    
    def save(self, *args, **kwargs):
        """
        Override the save method to clear the cache when the user is saved. Invalidate the Cache
        """
        super().save(*args, **kwargs)
        cache_key = f"user_profile_{self.id}"
        cache.delete(cache_key)
