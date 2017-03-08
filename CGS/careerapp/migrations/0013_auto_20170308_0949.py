# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0012_remove_course_programme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='prereq',
        ),
        migrations.AddField(
            model_name='programme',
            name='prereq',
            field=models.ForeignKey(blank=True, null=True, to='careerapp.Subject'),
        ),
    ]
