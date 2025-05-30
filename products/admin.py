from django.contrib import admin

from products.models import ProductImage, Product, ProductCategory, Poster, ColorProduct


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("product_title",)}


admin.site.register(ProductCategory)
admin.site.register(Poster)
admin.site.register(ColorProduct)
