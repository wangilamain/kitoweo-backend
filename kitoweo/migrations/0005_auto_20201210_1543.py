# Generated by Django 3.1.3 on 2020-12-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitoweo', '0004_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
