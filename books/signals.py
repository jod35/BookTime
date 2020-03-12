from io import BytesIO
import logging
from PIL import Image
from django.core.files.base import ContentFile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductImage

THUMBNAIL_SIZE=(300,300)

logger=logging.getLogger(__name__)

@receiver(pre_save,sender=ProductImage)
def generate_thumbnail(sender,instance,**kwargs):
    logger.info(
        "Generating Thumbnail for product %d",
        instance.product.id,
    )

    image=Image.open(instance.image)
    image=image.convert("RGB")
    image.thumbnail(THUMBNAIL_SIZE,Image.ANTIALIAS)
    tempthumb=BytesIO()
    image.save(tempthumb,"JPEG")
    tempthumb.seek(0)

    #set instance to false otherwise an infinite loop
    instance.thumbnail.save(
        ContentFile(tempthumb.read()),
        save=False,
    )
    tempthumb.close()
