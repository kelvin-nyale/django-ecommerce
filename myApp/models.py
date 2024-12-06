from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('seller', 'Seller'), ('user', 'User')])
    date_registered = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone']

    def __str__(self):
        return self.user_name


# class Users(models.Model):
#     user_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=50)
#     user_role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('seller', 'Seller'), ('user', 'User')])
#     date_registered = models.DateField(auto_now_add=True)
#     password = models.CharField(max_length=150)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email', 'user_role']
#
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
#
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)
#
#     def __str__(self):
#         return self.user_name


class Products(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    price = models.FloatField()

    def __str__(self):
        return self.product_name

class Services(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.service_name

class Categories(models.Model):
    category_id = models.CharField(unique=True, max_length=20)
    category_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category_name

# class ProductCategories(models.Model):
#     category_id = models.IntegerField(primary_key=True)
#     category_name = models.CharField(max_length=50)
#     description = models.TextField(truncatewords(100))
#     price = models.FloatField()
#
#     def __str__(self):
#         return self.category_name







