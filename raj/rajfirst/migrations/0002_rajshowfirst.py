# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rajfirst', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rajshowfirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rajshowemail', models.CharField(max_length=30)),
                ('rajshowuser', models.ManyToManyField(to='rajfirst.rajuserfirst')),
            ],
        ),
    ]