from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'product', api.ProductViewSet)
router.register(r'category', api.CategoryViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Product
    path('product_manager/product/', views.ProductListView.as_view(), name='product_manager_product_list'),
    path('product_manager/product/create/', views.ProductCreateView.as_view(), name='product_manager_product_create'),
    path('product_manager/product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_manager_product_detail'),
    path('product_manager/product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_manager_product_update'),
)

urlpatterns += (
    # urls for Category
    path('product_manager/category/', views.CategoryListView.as_view(), name='product_manager_category_list'),
    path('product_manager/category/create/', views.CategoryCreateView.as_view(), name='product_manager_category_create'),
    path('product_manager/category/detail/<slug:slug>/', views.CategoryDetailView.as_view(), name='product_manager_category_detail'),
    path('product_manager/category/update/<slug:slug>/', views.CategoryUpdateView.as_view(), name='product_manager_category_update'),
)

