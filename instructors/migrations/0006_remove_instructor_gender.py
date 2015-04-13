# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_auto_20150412_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='gender',
        ),
    ]
