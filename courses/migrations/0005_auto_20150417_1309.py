# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150417_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='number',
            field=models.PositiveIntegerField(),
            preserve_default=True,
        ),
    ]
