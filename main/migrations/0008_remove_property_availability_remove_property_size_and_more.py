# Generated by Django 5.0 on 2024-01-30 09:07

import django.db.models.deletion
import main.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_images_propertyimage_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='property',
            name='size',
        ),
        migrations.RemoveField(
            model_name='property',
            name='society',
        ),
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='date_of_availability',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='property',
            name='ready_to_move',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='area_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='balcony',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.property_subfolder),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.property'),
        ),
    ]
