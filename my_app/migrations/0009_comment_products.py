# Generated by Django 4.2.5 on 2023-12-28 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_remove_comment_blog_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.product'),
        ),
    ]