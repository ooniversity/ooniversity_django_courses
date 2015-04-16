# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0005_auto_20150416_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
    ]
