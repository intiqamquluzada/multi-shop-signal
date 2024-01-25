from modeltranslation.translator import TranslationOptions, register
from my_app.models import (Category, Color,
                          Product,
                          SpecialOffer,
                          Slider,)

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ("name", )

@register(Color)
class ColorTranslation(TranslationOptions):
    fields = ("name", )

@register(Product)
class ProductTranslation(TranslationOptions):
    fields = (
        "name",
        "description_L",
        "description_B",
        "information",
    )

@register(SpecialOffer)
class SpecialOfferTranslation(TranslationOptions):
    fields = ("text", )

@register(Slider)
class SliderTranslation(TranslationOptions):
    fields = ("title", "text")
