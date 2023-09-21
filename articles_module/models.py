from django.db import models
from Register_module.models import User
from jalali_date import date2jalali, datetime2jalali


# Create your models here.

# Categories Articles

class articles_category(models.Model):
    parent = models.ForeignKey('articles_category', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name='عنوان دسته بندی مقالات')
    url_title = models.CharField(max_length=300, verbose_name='لینک دسته بندی مقالات', unique=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'


# مقالات
class article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان دسته بندی مقالات')
    slug = models.SlugField(max_length=300, db_index=True, allow_unicode=True, verbose_name='لینک مقاله')
    images = models.ImageField(upload_to='images/article_images', verbose_name='تصویر مقاله')
    short_descriptions = models.TextField(verbose_name='توضیحات کوتاه مقاله')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان')
    Article_and_Category_Relation = models.ManyToManyField(articles_category,
                                                           verbose_name='ارتباط بین دسته بندی و مقاله')
    text = models.TextField(verbose_name='متن مقاله')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ مقاله')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, verbose_name='کاربر مقاله')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال', default=True)

    def __str__(self):
        return self.title

    def jalali_create_date(self):
        return date2jalali(self.create_date)

    def jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقالات سایت'
        verbose_name_plural = 'ماژول مقالات سایت'
