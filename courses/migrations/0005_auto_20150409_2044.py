# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150409_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='number',
            new_name='index_numer',
        ),
    ]
