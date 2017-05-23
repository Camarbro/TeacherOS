# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 12:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TeacherOS', '0002_activities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('Student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TeacherOS.Student')),
                ('Teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
