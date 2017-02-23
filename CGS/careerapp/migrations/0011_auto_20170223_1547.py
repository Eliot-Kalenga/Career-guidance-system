# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0010_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='course',
            name='prereq',
        ),
    ]
