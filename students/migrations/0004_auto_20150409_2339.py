# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20150409_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='birdth_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
