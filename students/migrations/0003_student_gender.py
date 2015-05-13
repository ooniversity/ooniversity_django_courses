# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default=True, max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Man'), (b'W', b'Woman')]),
            preserve_default=False,
        ),
    ]
