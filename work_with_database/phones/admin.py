from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'slug']
    list_filter = ['name', 'price']
    prepopulated_fields = {'slug': ['name']}