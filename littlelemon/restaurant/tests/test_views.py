from django.test import TestCase 
from models import MenuItem
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

#TestCase class
class MenuViewTest(TestCase):
     def test_get_item(self):
        print('sellllf',self)
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name="Pizza", description="Delicious pizza", price=10.99)
        self.menu2 = MenuItem.objects.create(name="Burger", description="Juicy burger", price=8.99)

    def test_getall(self):
        url = reverse('menu-list')  # Assuming you have a 'menu-list' URL in your urlpatterns
        response = self.client.get(url)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)