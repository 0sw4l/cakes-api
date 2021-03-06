# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-19 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('url_imagen', models.URLField()),
                ('precio', models.PositiveIntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Producto',
            },
        ),
    ]
