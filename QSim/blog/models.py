from django.db import models
from django import forms

# New imports added for ParentalKey, Orderable, InlinePanel, ImageChooserPanel

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet
import numpy as np
from PIL import Image

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):

    intro = models.CharField(max_length=250)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    domains = models.CharField(max_length=250, blank=True) # Not a charfield, a list.
    dominant_hex = models.CharField(max_length=250, default="#000000") # Not a charfield, a list.
    dominant_rgb = models.CharField(max_length=250, default="rgb(255,255,255)") # Not a charfield, a list.
    body = StreamField([ #Add symbols.
        ('topic', blocks.StructBlock([
            ('heading', blocks.CharBlock()),
            ('entrance', blocks.RichTextBlock()),
        ])),
        ('paragraph', blocks.RichTextBlock()),
        ('quotation', blocks.StructBlock([
            ('quote', blocks.RichTextBlock()),
            ('author', blocks.CharBlock()),
        ])),
        ('visual', blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('originalArtWork', ImageChooserBlock(required=False)),
            ('caption', blocks.CharBlock()),
        ])),
        ('symbol', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    def domains_as_list(self):
        return self.domains.split(',')

    def main_image(self):
        gallery_item = self.gallery_images.first()
        img = Image.open(gallery_item.image, 'r').convert('RGB')
        
        if gallery_item:
            return gallery_item.image
        else:
            return None

    # Get color of main image here. Save the color name and send it to the html. Careful, takes a lot of time to get a color.

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('domains'),
        FieldPanel('dominant_rgb'),
        FieldPanel('dominant_hex'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]