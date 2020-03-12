from django.test import TestCase
from books import models
from django.core.files.images import ImageFile
from decimal import Decimal

class TestSignal(TestCase):
    def test_signal_works_on_save(self):
        product = models.Product(
            name = "The Root of all Evil",
            price = Decimal("10.00"),
        )
        product.save()

        with open("books/fixtures/the-root-of-all-evil.jpg","rb") as f:
            
            image=models.ProductImage(product = product,image=ImageFile(f,name='trcoe.jpg'),)
            
            with self.assertLogs("main",level = "INFO") as cm:
                image.save()
        
        self.assertGreaterEqual(len(cm.output),1)
        image.refresh_from_db()

        with open("main/fixtures/the_root_of_all_evil.jpg",'rb') as f:
            expected_content=f.read()
            assert image.thumbnail.read() == expected_content
            image.thumbnail.delete(save=False)
            image.image.delete(save=False)
            





