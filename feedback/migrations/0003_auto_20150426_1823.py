# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20150426_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e:'),
            preserve_default=True,
        ),
    ]
