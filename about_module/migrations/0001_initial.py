# Generated by Django 4.2.4 on 2023-08-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_img', models.ImageField(upload_to='images/about_page', verbose_name='عکس درباره ما')),
                ('about_title', models.CharField(max_length=200, verbose_name='عنوان درباره ما')),
                ('about_text', models.TextField(max_length=200, verbose_name='توضیحات بیشتر درباره ما')),
            ],
            options={
                'verbose_name': 'بخش درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
    ]