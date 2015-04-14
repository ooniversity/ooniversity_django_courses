# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150408_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_last_name',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
