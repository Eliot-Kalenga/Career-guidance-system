# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0009_auto_20161228_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('duration', models.IntegerField(default=4)),
                ('School', models.ManyToManyField(to='careerapp.School')),
                ('career', models.ManyToManyField(blank=True, to='careerapp.CareerPathway')),
                ('faculty', models.ManyToManyField(to='careerapp.Faculty')),
                ('prereq', models.ManyToManyField(blank=True, null=True, to='careerapp.Subject')),
                ('programme', models.ForeignKey(to='careerapp.Programme')),
            ],
        ),
    ]
