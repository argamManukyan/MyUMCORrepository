from django.contrib import admin
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin, TranslationTabularInline
from .models import *


class NewsImageTabularInline(admin.TabularInline):
    model = NewsImages
    extra = 4


class PlainsImagesTabularInline(admin.TabularInline):
    model = PlainsImages
    extra = 4


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageTabularInline]


class PlainsAdmin(admin.ModelAdmin):
    inlines = [PlainsImagesTabularInline]


admin.site.register(News, TabbedDjangoJqueryTranslationAdmin)
admin.site.register(Plains, TabbedDjangoJqueryTranslationAdmin)

admin.site.register(PlainsCategory)
admin.site.register(AboutUs, TabbedDjangoJqueryTranslationAdmin)
admin.site.register(AboutUsCategory)
admin.site.register(MainContent, TabbedDjangoJqueryTranslationAdmin)
admin.site.register(Donate,TabbedDjangoJqueryTranslationAdmin)
admin.site.register(Slider)
