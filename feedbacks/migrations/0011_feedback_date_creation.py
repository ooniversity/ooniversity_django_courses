# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0010_remove_feedback_date_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_creation',
            field=models.DateTimeField(default=datetime.date(2015, 4, 25), verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', auto_now_add=True),
            preserve_default=False,
        ),
    ]
