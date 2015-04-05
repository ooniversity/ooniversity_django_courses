# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_completedtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='max_score',
            field=models.IntegerField(default=100, choices=[(50, b'50'), (100, b'100'), (200, b'200'), (300, b'300')]),
        ),
    ]
