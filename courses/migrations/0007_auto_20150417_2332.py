# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150417_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.PositiveIntegerField(unique=b'True', verbose_name=b'Number of lesson'),
            preserve_default=True,
        ),
    ]
