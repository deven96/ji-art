# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=120)),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to=b'albums')),
                ('tags', models.CharField(max_length=250)),
                ('is_visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=70), unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'albums')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to=b'albums')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=models.CharField(default=uuid.uuid4, max_length=255), editable=False, max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
            ],
        ),
    ]
