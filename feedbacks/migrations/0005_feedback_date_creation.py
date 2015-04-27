# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_remove_feedback_date_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_creation',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', null=True),
            preserve_default=True,
        ),
    ]
