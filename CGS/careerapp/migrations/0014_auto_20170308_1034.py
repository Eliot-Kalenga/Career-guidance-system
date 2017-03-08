# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0013_auto_20170308_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='corequisite_course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('course_code', models.CharField(max_length=300, blank=True)),
                ('course_name', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prerequisite_course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('course_code', models.CharField(max_length=300, blank=True)),
                ('course_name', models.CharField(max_length=300, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='School',
            new_name='institution',
        ),
        migrations.RemoveField(
            model_name='course',
            name='career',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='Department',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='Prerequisite',
            field=models.ManyToManyField(blank=True, to='careerapp.Prerequisite_course'),
        ),
        migrations.AddField(
            model_name='course',
            name='corequisite',
            field=models.ManyToManyField(blank=True, to='careerapp.corequisite_course'),
        ),
    ]
