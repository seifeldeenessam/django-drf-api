from rest_framework import  generics

from .serializers import CartSerializer
from .models import Cart

class CartListView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
