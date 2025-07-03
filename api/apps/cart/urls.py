from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartListView.as_view(), name='cart-list'),
]
