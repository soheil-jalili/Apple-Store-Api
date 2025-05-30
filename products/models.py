import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


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


class Product(models.Model):
    product_title = models.CharField(max_length=255)
    product_sub_title = models.CharField(max_length=255, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.IntegerField()
    sales_count = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    icon = models.FileField(upload_to='products/icons/', validators=[validate_image_or_svg], null=True, blank=True)
    is_slider = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title

    def save(self, *args, **kwargs):
        if self.product_title:
            self.slug = slugify(self.product_title, allow_unicode=True)

        super().save(*args, **kwargs)


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
