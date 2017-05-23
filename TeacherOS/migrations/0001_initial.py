# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=75)),
                ('DueDate', models.DateField()),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherOS.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='Students',
            field=models.ManyToManyField(to='TeacherOS.Student'),
        ),
    ]
