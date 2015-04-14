# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20150411_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='position',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
