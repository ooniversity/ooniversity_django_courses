# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150418_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='courset',
            new_name='courses',
        ),
    ]
