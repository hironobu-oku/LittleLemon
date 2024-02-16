from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuModel
from restaurant.serializers import MenuSerializers
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu_item1 = MenuModel.objects.create(name="AAA", price=123.00)
        self.menu_item2 = MenuModel.objects.create(name="BBB", price=456.00)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-list')
        response = client.get(url)

        expected_data = MenuSerializers([self.menu_item1, self.menu_item2], many=True).data

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data, expected_data)
