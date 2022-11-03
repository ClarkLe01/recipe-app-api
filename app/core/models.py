from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Manage for users"""

    def create_user(self, email, password=None, **extra_field):
        """Create, save and return a new user"""
        user = self.model(email=email, password=password, **extra_field)
        user.set_password(password)
        user.save(using=self.db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

