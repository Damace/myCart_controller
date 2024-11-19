from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),  # List and create products
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),  # Retrieve, update, delete products by ID
]