# Generated by Django 5.0 on 2023-12-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_color_size_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]