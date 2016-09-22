# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('members', models.ManyToManyField(to='measurements.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('altitude', models.IntegerField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('value', models.FloatField(default=0)),
                ('date', models.DateTimeField(verbose_name='date taken')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurements.Location')),
            ],
        ),
    ]
