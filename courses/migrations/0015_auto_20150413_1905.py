# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20150413_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
