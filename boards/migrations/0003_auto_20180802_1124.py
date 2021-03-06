# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-02 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20180607_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=1855),
        ),
        migrations.AlterField(
            model_name='board',
            name='status',
            field=models.CharField(choices=[('1normal', '일반'), ('3notice', '공지'), ('4warning', '신고접수'), ('6deleted', '삭제됨'), ('5hidden', '관리자 삭제'), ('2temp', '임시저장')], default='1normal', max_length=10),
        ),
        migrations.AlterField(
            model_name='reply',
            name='image',
            field=models.ImageField(blank=True, upload_to='reply-images/%Y-%m-%d/'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_to',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='reply',
            name='status',
            field=models.CharField(choices=[('1normal', '일반'), ('6deleted', '삭제됨'), ('5hidden', '관리자 삭제')], default='1normal', max_length=10),
        ),
    ]
