# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerapp', '0011_auto_20170223_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='programme',
        ),
    ]
