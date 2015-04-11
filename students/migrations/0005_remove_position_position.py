# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20150410_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='position',
        ),
    ]
