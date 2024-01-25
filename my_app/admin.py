from django.contrib import admin
from my_app.models import *

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Comment)
admin.site.register(Partniors)
admin.site.register(SpecialOffer)
admin.site.register(Slider)
admin.site.register(Basket)
admin.site.register(SignUp)
admin.site.register(SosialMedia)