from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from time import time
from unidecode import unidecode

def generate_slug(s):
    new_slug = slugify(unidecode(s))
    return new_slug + '-' + str(int(time()))


class AboutUsCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    text = models.TextField(blank=True)
    image = models.FileField(upload_to='about/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    category = models.ForeignKey(AboutUsCategory, on_delete=models.SET_NULL, null=True, related_name='abouts')
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    image = models.FileField(upload_to='about/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news.title


class PlainsCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    text = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='plains_category_images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Plains(models.Model):
    category = models.ForeignKey(PlainsCategory, on_delete=models.CASCADE, related_name='plains')
    name = models.CharField(max_length=120)
    text = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PlainsImages(models.Model):
    plain = models.ForeignKey(Plains, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='plains/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plain.name


class Slider(models.Model):
    image = models.FileField(upload_to='slider/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.path


class MainContent(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Donate(models.Model):
    sphere = models.ForeignKey(PlainsCategory, on_delete=models.CASCADE)
    target_group = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    total_amount = models.FloatField(default=0.0)
    donated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sphere.name} - {self.target_group} - {self.total_amount} USD"
