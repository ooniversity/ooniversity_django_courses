# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20150411_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([]),
        ),
    ]
