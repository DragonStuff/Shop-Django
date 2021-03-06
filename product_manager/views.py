""" This file controls the views for Products and Categories inside product_manager. """

# Django imports
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

# Project imports
from .models import Product, Category
from .forms import ProductForm


class IndexView(ListView):
    """ This index view displays the last ten products created. """
    template_name = 'product_manager/index.html'
    
    def get_queryset(self):
            """ Return the last ten products. """
            return Product.objects.order_by('-id')[:10]


class ProductListView(ListView):
    """ Allows you to list all products. """
    model = Product


class ProductCreateView(CreateView):
    """ Allows you to create a product (linked to forms). """
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    """ Allows you to view detailed information about an object in Product. """
    model = Product


class ProductDeleteView(DeleteView):
    """ Allows you to delete a product. """
    model = Product
    success_url = reverse_lazy('product_manager_product_list')


class ProductUpdateView(UpdateView):
    """ Allows you to update a product's details. """
    model = Product
    form_class = ProductForm


class CategoryListView(ListView):
    """ Allows you to view all categories. """
    model = Category


class CategoryDetailView(DetailView):
    """ Allows you to view details of a category (will be used for inline product display). """
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of the current category taken from above context.
        context['products_in_category'] = Product.objects.filter(category=context['object'])
        return context
