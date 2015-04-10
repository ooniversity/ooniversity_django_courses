# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=256, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
            preserve_default=True,
        ),
    ]
