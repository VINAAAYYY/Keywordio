from unicodedata import name
from django.db import models
#from django.forms import *
from django.db.models.fields import *
from django.forms import ImageField
from sqlalchemy import false
from datetime import date
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

# Create your models here.
class Books(models.Model):
    name = CharField(max_length=50, blank=True, null=True)
    genre = CharField(max_length=100, blank=True, null=True)
    author = CharField(max_length=50, blank=True, null=True)
    bestseller = BooleanField(default=False, blank=True, null=True)
    description = TextField(blank=True, null=True)
    published_on = DateField(default=date.today, blank=True, null=True) 
