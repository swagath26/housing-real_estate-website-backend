# Generated by Django 5.0 on 2024-01-20 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20231205_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='image',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_files', to='main.property'),
        ),
        migrations.DeleteModel(
            name='PropertyImageName',
        ),
    ]
