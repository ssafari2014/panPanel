# Generated by Django 4.2.4 on 2023-08-25 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر مقاله'),
        ),
    ]