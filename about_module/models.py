from django.db import models


# Create your models here.

class AboutModel(models.Model):
    about_background_img = models.ImageField(upload_to='images/about_page/background_img', verbose_name= 'پس ضمینه ی  درباره ما', null=True)
    about_img = models.ImageField(upload_to='images/about_page', verbose_name='عکس درباره ما')
    about_title = models.CharField(max_length=200, verbose_name='عنوان درباره ما')
    about_text = models.TextField(max_length=200, verbose_name='توضیحات بیشتر درباره ما')

    def __str__(self):
        return self.about_title

    class Meta:
        verbose_name = 'بخش درباره ما'
        verbose_name_plural = 'درباره ما'

