# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150408_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='adress',
            new_name='address',
        ),
    ]
