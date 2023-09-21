from django.db import models


# Create your models here.

class ContactusModel(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='نام ')
    last_name = models.CharField(max_length=200, verbose_name='نام خانوادگی ')
    subject = models.CharField(max_length=200, verbose_name='عنوان ')
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان', null=True)
    See_message = models.BooleanField(verbose_name='خوانده شده', default=False)
    message = models.TextField(verbose_name='متن پیام کاربر')
    Answer_admin = models.TextField(verbose_name='متن پیام ادمین', null=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'صفحه تماس با ما'
        verbose_name_plural = 'تماس با ما سایت'
