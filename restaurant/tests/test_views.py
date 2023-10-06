from django.test import TestCase

from ..models import Menu


class MenuViewTest(TestCase):

    def setUp(self) -> None:
        Menu.objects.create(id=1, title="Icecream", price=1.99, inventory=100)
        Menu.objects.create(id=2, title="Pasta", price=5.99, inventory=60)
        Menu.objects.create(id=3, title="Pizza", price=12.99, inventory=50)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/1')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('/restaurant/menu/2')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('/restaurant/menu/3')
        self.assertEquals(response.status_code, 200)

        response = self.client.get('/restaurant/menu/4')
        self.assertEquals(response.status_code, 404)

    def tearDown(self) -> None:
        pass
