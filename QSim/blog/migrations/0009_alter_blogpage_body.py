# Generated by Django 3.2.2 on 2022-02-26 07:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('topic', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('entrance', wagtail.core.blocks.CharBlock())])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('quotation', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.RichTextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('visual', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock())]))]),
        ),
    ]
