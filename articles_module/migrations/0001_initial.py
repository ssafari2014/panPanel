# Generated by Django 4.2.4 on 2023-08-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان دسته بندی مقالات')),
                ('url_title', models.CharField(max_length=300, unique=True, verbose_name='لینک دسته بندی مقالات')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles_module.articles_category')),
            ],
            options={
                'verbose_name': 'دسته بندی مقالات',
                'verbose_name_plural': 'دسته بندی های مقالات',
            },
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان دسته بندی مقالات')),
                ('slug', models.SlugField(allow_unicode=True, max_length=300, verbose_name='لینک مقاله')),
                ('images', models.ImageField(upload_to='images/article_images', verbose_name='تصویر مقاله')),
                ('short_descriptions', models.TextField(verbose_name='توضیحات کوتاه مقاله')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان')),
                ('text', models.TextField(verbose_name='متن مقاله')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('Article_and_Category_Relation', models.ManyToManyField(to='articles_module.articles_category', verbose_name='ارتباط بین دسته بندی و مقاله')),
            ],
            options={
                'verbose_name': 'مقالات سایت',
                'verbose_name_plural': 'ماژول مقالات سایت',
            },
        ),
    ]
