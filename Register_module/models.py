from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Creating my own user model

class User(AbstractUser):
    number = models.CharField(max_length=200, verbose_name='شماره')
    email_active_code = models.CharField(max_length=200, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'نام کاربری'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
