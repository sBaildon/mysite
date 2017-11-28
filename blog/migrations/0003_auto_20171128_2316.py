# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 15:16
from __future__ import unicode_literals

import blog.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160811_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_img',
            field=models.FileField(default='/media/default.png', storage=blog.storage.OverwriteStorage(), upload_to=''),
        ),
    ]
