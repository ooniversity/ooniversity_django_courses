# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='coach_sex',
            field=models.CharField(default=b'\xd0\x9c\xd1\x83\xd0\xb6', max_length=3, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'\xd0\x9c\xd1\x83\xd0\xb6', b'\xd0\xbc\xd1\x83\xd0\xb6\xd1\x87\xd0\xb8\xd0\xbd\xd0\xb0'), (b'\xd0\x96\xd0\xb5\xd0\xbd', b'\xd0\xb6\xd0\xb5\xd0\xbd\xd1\x89\xd0\xb8\xd0\xbd\xd0\xb0')]),
            preserve_default=True,
        ),
    ]
