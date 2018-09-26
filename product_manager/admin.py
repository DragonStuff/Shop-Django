from django.contrib import admin
from django import forms
from .models import Product, Category

class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'slug', 'description', 'price']
    readonly_fields = ['name', 'slug', 'description', 'price']

admin.site.register(Product, ProductAdmin)


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'slug']
    readonly_fields = ['name', 'slug']

admin.site.register(Category, CategoryAdmin)


