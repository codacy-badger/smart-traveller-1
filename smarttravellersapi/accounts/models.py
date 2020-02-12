from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    """
    Class for creating user implementing the abstract base user and the permission class.
    """
    username = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=25,blank=True,null=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username','email','first_name', 'last_name']

    def __str__(self):
        """Returns a string representation of this `User`."""
        return "{}".format(self.mobile)

class Agent(CustomUser):
    station = models.TextField(max_length=50,unique=True)
    present_address = models.TextField(max_length=100,unique=True)
    permanent_address = models.TextField(max_length=100,unique=True)

    def __str__(self):
        """Returns a string representation of this `Agent`."""
        return self.mobile
