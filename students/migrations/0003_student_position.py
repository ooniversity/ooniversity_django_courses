# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150410_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='position',
            field=models.CharField(default='student', max_length=20, choices=[(b'student', b'Student'), (b'laborant', b'Laborant')]),
            preserve_default=False,
        ),
    ]
