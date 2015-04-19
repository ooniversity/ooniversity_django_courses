# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150416_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='num',
            field=models.PositiveIntegerField(help_text=b'dsdsda'),
            preserve_default=True,
        ),
    ]
