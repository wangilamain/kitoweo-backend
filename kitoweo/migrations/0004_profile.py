# Generated by Django 3.1.3 on 2020-12-10 15:14

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitoweo', '0003_auto_20201210_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('image', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='Profile pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitoweo.user')),
            ],
        ),
    ]