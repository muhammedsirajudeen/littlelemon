from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(name='Pizza', price=10.99, category='Main')
        Menu.objects.create(name='Salad', price=5.99, category='Starter')

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu-list')
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
