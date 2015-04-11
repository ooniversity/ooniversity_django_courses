# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(max_length=255, verbose_name='Lesson theme'),
            preserve_default=True,
        ),
    ]
