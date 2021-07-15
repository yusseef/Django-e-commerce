from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=200, choices=STATUS)
    slug = models.SlugField(null= False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
        
    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
        
class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) #many to one 
    title = models.CharField(max_length=500)
    keywords = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    detail = RichTextUploadingField(null=True)
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=200, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_details', kwargs= {'slug': self.slug})

    @property
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""

class Images(models.Model):
    product=models.ForeignKey(Product,related_name="images", on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    