
from django.contrib import admin
from .models import Category, Product, Images
# Register your models here.

class CatgeoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]


class ImageAdmin(admin.ModelAdmin):
    list_display=['image', 'title',]

admin.site.register(Category, CatgeoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)