from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    phone = PhoneNumberField(blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, max_length=50)
    smtpserver = models.CharField(max_length=50, blank=True)
    smtpemail = models.CharField(max_length=50, blank=True)
    smtppassword = models.CharField(blank=True, max_length=50)
    smtpport = models.CharField(max_length=50, blank=True)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
     )
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, default="New", max_length=50)
    ip = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs = {'class': 'input', 'placeholder': 'Name'}),
            'subject': TextInput(attrs = {'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs = {'class': 'input', 'placeholder': 'Email'}),
            'Messages': Textarea(attrs = {'class': 'input', 'placeholder': 'Your messages', 'rows': '5'}),
        }