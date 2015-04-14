# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_coach_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='desc',
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(max_length=2, choices=[(b'1', b'Male'), (b'2', b'Famale')]),
            preserve_default=True,
        ),
    ]
