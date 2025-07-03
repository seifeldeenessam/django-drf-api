from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products-list'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('media/<str:name>/', views.ProductImageView.as_view(), name='product-image'),
]
