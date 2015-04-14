# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20150410_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='name',
        ),
    ]
