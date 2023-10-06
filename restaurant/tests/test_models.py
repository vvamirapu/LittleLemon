from django.test import TestCase

from ..models import Menu


class MenuTest(TestCase):
    def test_item(self):
        item = Menu(title="Icecream", price="1.99", inventory=100)
        self.assertEquals(item.__str__(), "Icecream : 1.99")
