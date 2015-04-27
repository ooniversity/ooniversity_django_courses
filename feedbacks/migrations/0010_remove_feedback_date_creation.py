# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0009_auto_20150425_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date_creation',
        ),
    ]
