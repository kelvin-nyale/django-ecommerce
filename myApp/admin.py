from django.contrib import admin
from .models import Users, Products, Services, Categories

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Services)
admin.site.register(Categories)