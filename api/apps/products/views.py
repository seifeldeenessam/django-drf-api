from rest_framework import  generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse, Http404
from django.conf import settings
import os
import mimetypes

from .serializers import ProductSerializer
from .models import Product

class ProductsListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductImageView(APIView):
    def get(self, request, name):
        try:
            # Security: prevent directory traversal
            if '..' in name or name.startswith('/'):
                return Response(
                    {'error': 'Invalid file name'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Construct the file path
            file_path = os.path.join(settings.MEDIA_ROOT, name)

            # Ensure the file is within MEDIA_ROOT
            if not file_path.startswith(settings.MEDIA_ROOT):
                return Response(
                    {'error': 'Invalid file path'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Check if file exists
            if not os.path.exists(file_path):
                raise Http404("Image not found")

            # Detect content type
            content_type, _ = mimetypes.guess_type(file_path)
            if not content_type or not content_type.startswith('image/'):
                return Response(
                    {'error': 'File is not an image'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Return the file
            return FileResponse(
                open(file_path, 'rb'),
                content_type=content_type
            )
        except Http404:
            return Response(
                {'error': 'Image not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': 'Server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
