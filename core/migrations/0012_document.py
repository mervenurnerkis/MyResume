# Generated by Django 3.2.7 on 2023-11-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('slug', models.SlugField(blank=True, max_length=254, verbose_name='Slug')),
                ('button_text', models.CharField(blank=True, max_length=254, verbose_name='Button Text')),
                ('file', models.FileField(blank=True, upload_to='documents/', verbose_name='File')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]