# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_auto_20150411_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'1', b'M'), (b'2', b'F')]),
            preserve_default=True,
        ),
    ]
