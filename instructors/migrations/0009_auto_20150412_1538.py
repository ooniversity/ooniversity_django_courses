# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0008_auto_20150412_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
