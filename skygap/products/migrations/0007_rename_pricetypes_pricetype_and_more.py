# Generated by Django 4.2.2 on 2023-08-01 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('products', '0006_pricetypes_productprice_product_price_types'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PriceTypes',
            new_name='PriceType',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_types',
        ),
    ]
