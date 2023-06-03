from django.urls import path
from .views import ProtectedView, ProductDetailAPIView

urlpatterns = [
    path("protected/", ProtectedView.as_view(), name="protected"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
]
