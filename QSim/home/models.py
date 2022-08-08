from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel



class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        img = Image.open(gallery_item.image, 'r').convert('RGB')
        
        if gallery_item:
            return gallery_item.image
        else:
            return None

class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    dominantColor = models.CharField(blank=True, max_length=250)
    deity = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
        FieldPanel('deity'),
        FieldPanel('dominantColor'),
    ]