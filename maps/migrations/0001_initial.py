# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=16)),
                #('picture', models.ImageField(upload_to=b'')),
                ('picture', models.ImageField(upload_to=settings.IMAGE_DIR)),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]
