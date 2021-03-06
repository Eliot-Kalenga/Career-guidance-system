# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-10 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0007_auto_20161108_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerapp.CareerCluster')),
            ],
        ),
    ]
