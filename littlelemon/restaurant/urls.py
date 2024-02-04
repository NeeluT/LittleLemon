#define URL route for index() view
from django.urls import path
from . import views
from .views import BookingViewSet, CustomRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsViewSet),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', BookingViewSet.as_view()),
    path('api-token-auth/', obtain_auth_token),
]