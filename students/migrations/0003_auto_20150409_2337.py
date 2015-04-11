# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='students',
            name='kontr_count',
        ),
        migrations.RemoveField(
            model_name='students',
            name='prakt_count',
        ),
        migrations.RemoveField(
            model_name='students',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='students',
            name='second_name',
        ),
        migrations.AddField(
            model_name='students',
            name='phone',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
    ]
