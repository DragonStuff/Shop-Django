from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Product, Category
from .forms import ProductForm, CategoryForm


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product


class ProductDeletionView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_manager_product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm


class CategoryDetailView(DetailView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm

