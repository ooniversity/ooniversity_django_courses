# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20150426_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='create_time',
        ),
        migrations.AlterField(
            model_name='letter',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438'),
            preserve_default=True,
        ),
    ]
