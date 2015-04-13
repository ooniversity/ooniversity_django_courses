# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0014_auto_20150412_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
