# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150409_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='topic',
            field=models.CharField(max_length=85),
            preserve_default=True,
        ),
    ]
