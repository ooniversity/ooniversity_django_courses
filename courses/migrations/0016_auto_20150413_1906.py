# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20150413_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
