# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_remove_coach_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
