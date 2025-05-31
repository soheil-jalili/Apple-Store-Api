import os

from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta


def validate_image_or_svg(file):
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if ext not in valid_extensions:
        raise ValidationError('Unsupported file extension. Only JPG, PNG, and SVG are allowed.')


class ProductCategory(models.Model):
    category_title = models.CharField(max_length=255)
    category_image = models.FileField(upload_to='categories/', validators=[validate_image_or_svg])
    category_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_title

    def save(
            self,
            *args, **kwargs
    ):
        if self.category_slug:
            if not self.category_slug.startswith('category-'):
                self.category_slug = f'category-{self.category_slug}'
        super().save(*args, **kwargs)


class ColorProduct(models.Model):
    name = models.CharField(max_length=50)
    code_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_title = models.CharField(max_length=255)
    product_sub_title = models.CharField(max_length=255, null=True, blank=True)
    product_description = RichTextField(null=True, blank=True)
    product_price = models.IntegerField()
    sales_count = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True, max_length=255)
    icon = models.FileField(upload_to='products/icons/', validators=[validate_image_or_svg], null=True, blank=True)
    is_slider = models.BooleanField(default=False)

    is_discounted = models.BooleanField(default=False)
    discount_price = models.IntegerField(null=True, blank=True)
    discount_end_time = models.DateTimeField(null=True, blank=True)

    colors = models.ManyToManyField(ColorProduct, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title

    def save(self, *args, **kwargs):
        if self.product_title:
            new_slug = slugify(self.product_title, allow_unicode=True)
            if not self.slug or self.slug != new_slug:
                self.slug = new_slug

        super().save(*args, **kwargs)

    def discount_time_left(self):
        if self.discount_end_time and timezone.now() < self.discount_end_time:
            delta = self.discount_end_time - timezone.now()
            return {
                'days': delta.days,
                'hours': delta.seconds // 3600,
                'minutes': (delta.seconds % 3600) // 60,
            }
        return None


def product_image_upload_path(instance, filename):
    product_slug = slugify(instance.product.product_title, allow_unicode=True)
    return f'products/{product_slug}/images/{filename}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to=product_image_upload_path)

    def __str__(self):
        return f'Image for {self.product.product_title}'


class Poster(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posters/')
    icon = models.FileField(upload_to='posters/icons/', validators=[validate_image_or_svg], null=True, blank=True)
    is_footer_poster = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
