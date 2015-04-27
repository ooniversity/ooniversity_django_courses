# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0005_delete_assistant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.IntegerField(default=1, max_length=1, choices=[(1, b'\xd0\x9c'), (2, b'\xd0\x96')]),
            preserve_default=True,
        ),
    ]
