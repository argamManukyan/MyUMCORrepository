from django.urls import path
from .views import *
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers



urlpatterns = [
    path('main/',MainAPI.as_view(),name='home'),
    path('abouts/',AboutAPI.as_view({'get': 'list'}),name='abouts'),
    path('abouts/<str:slug>/',AboutSingleAPI.as_view(),name='abouts_details'),
    path('news/',NewsAPI.as_view({'get': 'list'}),name='news'),
    path('news/<str:slug>/',NewsSingleAPI.as_view(),name='news_details'),
    path('plains/',PlainsAPI.as_view({'get': 'list'}),name='plains'),
    path('plains/<str:slug>/',PlainsSingleAPI.as_view(),name='plains_details'),
    path('slider/',SliderAPI.as_view({'get': 'list'}),name='slider'),
    path('donate/',DonateCreateAPI.as_view(),name='donate'),
    path('get_language/',get_language,name='get_language')


]
