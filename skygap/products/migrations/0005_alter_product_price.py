# Generated by Django 4.2.2 on 2023-08-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_emb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Iron-on Price ($)'),
        ),
    ]