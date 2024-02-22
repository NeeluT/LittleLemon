from django.test import TestCase 

# from restaurant.models import MenuItem
from models import MenuItem

#TestCase class
class MenuItemTest(TestCase):
     def test_get_item(self):
        print('sellllf',self)
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

