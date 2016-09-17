# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('grade', models.CharField(max_length=10)),
                ('photo', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
