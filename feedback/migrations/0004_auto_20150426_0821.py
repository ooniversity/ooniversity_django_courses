# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20150426_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='time',
        ),
        migrations.AddField(
            model_name='letter',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 8, 20, 22, 969936), verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='letter',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 8, 21, 2, 528299, tzinfo=utc), auto_now=True, auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438'),
            preserve_default=False,
        ),
    ]
