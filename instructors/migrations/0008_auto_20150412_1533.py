# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0007_instructor_linkein'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='edited_date',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='linkein',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='sulary',
        ),
        migrations.AddField(
            model_name='instructor',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
