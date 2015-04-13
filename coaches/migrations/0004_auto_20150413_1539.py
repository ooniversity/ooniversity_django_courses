# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20150413_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='coach_sex',
            field=models.CharField(default=b'1', max_length=6, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'1', b'\xd0\xbc\xd1\x83\xd0\xb6'), (b'2', b'\xd0\xb6\xd0\xb5\xd0\xbd')]),
            preserve_default=True,
        ),
    ]
