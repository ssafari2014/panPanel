from django.contrib import admin
from . import models


# Register your models here.
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


admin.site.register(models.site_setting)
admin.site.register(models.FooterLinkBoxModel)
admin.site.register(models.FooterLinkModel, FooterLinkAdmin)
