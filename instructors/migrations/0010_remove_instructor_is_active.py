# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0009_auto_20150412_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='is_active',
        ),
    ]
