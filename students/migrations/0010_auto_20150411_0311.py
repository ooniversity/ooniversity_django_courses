# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20150411_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
