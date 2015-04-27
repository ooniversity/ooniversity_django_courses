# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e:', blank=True),
            preserve_default=True,
        ),
    ]
