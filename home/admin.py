from django.contrib import admin
from .models import Setting, ContactMessage

class Settingadmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'updated_at', 'status' ]

class Messageadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status']
    readonly_fields = ['name', 'email', 'subject', 'message', 'ip']
    list_filter = ['status']


admin.site.register(Setting, Settingadmin)
admin.site.register(ContactMessage, Messageadmin)