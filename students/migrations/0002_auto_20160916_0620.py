# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
    ]
