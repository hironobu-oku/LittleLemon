from django.test import TestCase
from restaurant.models import MenuModel

class MenuTest(TestCase):
    def test_menu_representation(self):
        menu_item = MenuModel.objects.create(name="AAA", price=123)

        self.assertEqual(str(menu_item), "AAA - $123")

