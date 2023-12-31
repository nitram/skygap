# Generated by Django 4.2.2 on 2023-07-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('designs', '0003_remove_design_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Product type icon (<sizing guide>)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.DeleteModel(
            name='DesignImage',
        ),
    ]
