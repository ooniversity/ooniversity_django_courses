# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0007_auto_20150417_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
    ]
