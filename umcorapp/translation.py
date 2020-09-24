from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)


translator.register(AboutUs, AboutUsTranslationOptions)


# @register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


translator.register(News, NewsTranslationOptions)


class PlainsTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)


translator.register(Plains, PlainsTranslationOptions)


class MainTranslationOptions(TranslationOptions):
    fields = ('text',)


translator.register(MainContent, MainTranslationOptions)


class DonateTranslationOptions(TranslationOptions):
    fields = ('sphere', 'target_group',)


translator.register(Donate, DonateTranslationOptions)