# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20150409_0916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_last_name']},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('student_last_name', 'student_name')]),
        ),
    ]
