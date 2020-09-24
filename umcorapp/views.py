import json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils import translation
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.pagination import PageNumberPagination


def get_language(request):
    return JsonResponse(data={'language': request.LANGUAGE_CODE}, safe=False, status=200)


class NewsPageNumberPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class PlansPageNumberPagination(PageNumberPagination):
    page_size = 11

    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class MainAPI(ListAPIView):
    queryset = MainContent.objects.all()
    serializer_class = MainSerializer



class AboutAPI(viewsets.ModelViewSet):
    queryset = AboutUsCategory.objects.all()
    serializer_class = AboutUsCategorySerializer


class AboutSingleAPI(RetrieveAPIView):
    queryset = AboutUsCategory.objects.all()
    serializer_class = AboutUsCategorySerializer
    lookup_field = 'slug'


class NewsAPI(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    pagination_class = NewsPageNumberPagination


class NewsSingleAPI(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        current_news = News.objects.get(slug=kwargs['slug'])
        qs = News.objects.exclude(slug=kwargs['slug'])
        serializer = NewsSerializer(qs, many=True)
        serializer_two = NewsSerializer(current_news)
        return Response({'other_news': serializer.data, 'current_news': serializer_two.data}, status=HTTP_200_OK)


class PlainsAPI(viewsets.ModelViewSet):
    queryset = PlainsCategory.objects.all()
    serializer_class = PlainsCategorySerializer
    pagination_class = PlansPageNumberPagination


class PlainsSingleAPI(RetrieveAPIView):
    queryset = PlainsCategory.objects.all()
    serializer_class = PlainsCategorySerializer
    lookup_field = 'slug'


class SliderAPI(viewsets.ModelViewSet):
    queryset = Slider.objects.all().order_by('-id')[:3]
    serializer_class = SliderSerializer


class DonateCreateAPI(CreateAPIView):
    queryset = Donate.objects.all()
    serializer_class = DonateSerializer

    def post(self, request, *args, **kwargs):
        serializer = DonateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
