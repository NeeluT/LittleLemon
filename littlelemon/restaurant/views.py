from django.shortcuts import render

from rest_framework import viewsets, generics, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import BookingSerializer, UserCreateSerializer, MenuItemSerializer
from djoser.views import UserViewSet
from .serializers import CustomUserCreateSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

# class CustomUserCreateView(UserCreateView):
#     serializer_class = CustomUserCreateSerializer

class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserCreateSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer

# @api_view()
# @permission_classes([IsAuthenticated])

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     permission_classes = [IsAuthenticated]
    
class MenuItemsViewSet(viewsets.ViewSet, generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

# @api_view()
# @permission_classes([IsAuthenticated])
# # @authentication_classes([TokenAuthentication])
# def msg(request):
#      return Response({"message":"This view is protected"})