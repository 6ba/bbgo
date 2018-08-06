# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-02 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='featured_images/%Y-%m/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='like_users',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('6deleted', '삭제됨'), ('1normal', '발행됨'), ('2temp', '임시 글'), ('5hidden', '검토중')], default='1normal', max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('1normal', '일반'), ('6deleted', '삭제됨'), ('7spam', '스팸')], default='1normal', max_length=10),
        ),
    ]
