from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=200, choices=STATUS)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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
    detail = models.TextField(null=True)
    slug = models.SlugField()
    status = models.CharField(max_length=200, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
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
    