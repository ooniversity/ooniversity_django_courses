# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 17, 12, 43, 369709), blank=True),
            preserve_default=True,
        ),
    ]
