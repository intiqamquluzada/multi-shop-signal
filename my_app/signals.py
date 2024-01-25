from django.dispatch import receiver
from django.db.models.signals import post_save
from my_app.models import Product
from django.shortcuts import redirect


@receiver(post_save, sender=Product)
def my_func(instance, created, **kwargs):
    print("Hello")

