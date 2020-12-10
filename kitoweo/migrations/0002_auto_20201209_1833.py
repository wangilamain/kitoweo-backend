# Generated by Django 3.1.3 on 2020-12-09 18:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitoweo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='website',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='projectname',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='size/age'),
        ),
    ]
