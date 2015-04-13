# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0004_auto_20150411_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(unique=True, max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
