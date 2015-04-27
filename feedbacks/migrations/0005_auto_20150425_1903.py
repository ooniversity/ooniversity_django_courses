# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20150425_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 19, 3, 5, 729638), blank=True),
            preserve_default=True,
        ),
    ]
