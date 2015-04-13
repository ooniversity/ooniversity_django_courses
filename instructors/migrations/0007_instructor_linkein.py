# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0006_remove_instructor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='linkein',
            field=models.URLField(unique=True, null=True),
            preserve_default=True,
        ),
    ]
