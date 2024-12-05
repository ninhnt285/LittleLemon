from django.test import TestCase

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="IceCream", price=80.00, inventory=100)
        item2 = Menu.objects.create(title="Rice", price=100.00, inventory=100)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(serializer.data, [{
            'id': items[0].id,
            'title': 'IceCream',
            'price': '80.00',
            'inventory': 100,
        }, {
            'id': items[1].id,
            'title': 'Rice',
            'price': '100.00',
            'inventory': 100,
        }])