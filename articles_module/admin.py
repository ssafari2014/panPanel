from django.contrib import admin
from . import models
from .models import article

# Register your models here.
class articles_category_Admin(admin.ModelAdmin):
    list_display = [
        'title', 'url_title', 'is_active', 'parent'
    ]
    list_editable = [
        'is_active', 'parent'
    ]


class article_admin(admin.ModelAdmin):
    list_display = [
          'title', 'is_active', 'auther'
    ]
    list_editable = [
        'is_active',
    ]
    
    def save_model(self, request, obj: article, form, change):
        if not change:
            obj.auther = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.articles_category, articles_category_Admin)
admin.site.register(models.article, article_admin)
