# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0010_remove_instructor_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='position',
            field=models.CharField(default=b'instructor', max_length=10, choices=[(b'instructor', b'Instructor'), (b'assistant', b'Assistant')]),
            preserve_default=True,
        ),
    ]
