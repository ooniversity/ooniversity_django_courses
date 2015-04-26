# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pybursa_emails', '0004_auto_20150426_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 18, 51, 40, 469618), null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
