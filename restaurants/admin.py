from django.contrib import admin

from django.urls import path, include

from .models import Category, Restaurant

class CategoryAdmin(admin.ModelAdmin):
    ...

class RestaurantAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
