from rest_framework import serializers
from .models import *


class AboutsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta:
        model = AboutUs
        fields = "__all__"

class AboutUsCategorySerializer(serializers.ModelSerializer):


    abouts = AboutsSerializer(many=True,read_only=True)

    class Meta:
        model = AboutUsCategory
        fields = ('id','name','slug','abouts')


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImages
        fields = ('image',)
#
class NewsSerializer(serializers.ModelSerializer):

    images = NewsImageSerializer(many=True,read_only=True)
    class Meta:
        model = News
        fields = "__all__"


class PlainsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlainsImages
        fields = ('image',)
#

class PlainsSerializer(serializers.ModelSerializer):
    images = PlainsImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Plains
        fields = "__all__"

class PlainsCategorySerializer(serializers.ModelSerializer):


    plains = PlainsSerializer(many=True,read_only=True)

    class Meta:
        model = PlainsCategory
        fields = "__all__"

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ['image',]


class MainSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainContent
        fields = '__all__'


class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        fields = "__all__"
