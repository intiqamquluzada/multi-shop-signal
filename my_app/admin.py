from django.contrib import admin
from my_app.models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageAdmin]

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(Comment)
admin.site.register(Partniors)
admin.site.register(SpecialOffer)
admin.site.register(Slider)
admin.site.register(Basket)
admin.site.register(SignUp)
admin.site.register(SosialMedia)