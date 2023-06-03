from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from authentication.serializers import UserSerializer
from .models import Product


class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            data = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "photo": str(product.photo),
                "manufacturer": product.manufacturer,
                "seller": str(product.seller),
                "status": product.status,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )
