# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20150425_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 17, 59, 48, 546095), blank=True),
            preserve_default=True,
        ),
    ]
