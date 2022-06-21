from django.contrib import admin
from razorpay import Customer
from .models import Books, CustomUser
# Register your models here.

class customuserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

class bookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'genre', 'published_on' ]
    search_fields = ['name', 'author', 'genre']

admin.site.register(Books, bookAdmin)
admin.site.register(CustomUser, customuserAdmin)