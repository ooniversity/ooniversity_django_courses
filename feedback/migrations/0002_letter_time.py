# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 25, 10, 30, 59, 419017), verbose_name='\u0412\u0440\u0435\u043c\u044f'),
            preserve_default=True,
        ),
    ]
