from django.contrib import admin
from .models import Category, Item


# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass



admin.site.register(Item)