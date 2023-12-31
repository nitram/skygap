# Generated by Django 4.2.2 on 2023-08-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_productprice_types_productprice_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='types',
        ),
        migrations.RemoveField(
            model_name='product',
            name='emb_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Starting Price ($)'),
        ),
        migrations.DeleteModel(
            name='PriceType',
        ),
        migrations.DeleteModel(
            name='ProductPrice',
        ),
    ]
