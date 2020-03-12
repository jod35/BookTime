from decimal import Decimal
from django.test import TestCase
from books import models

class TestModel(TestCase):
    def test_sctive_manager_works(self):
        models.Product.objects.create(
            name="The Root of all Evil",
            price=Decimal("10.00"),
        )
        models.Product.objects.create(
            name="The fall of Amin",
            price=Decimal("2.00"),
        )
        models.Product.objects.create(
            name="The rise of the Termite",
            price=Decimal("2.00"),
            active=False
        )
        self.assertEqual(len(models.Product.objects.active()),2)