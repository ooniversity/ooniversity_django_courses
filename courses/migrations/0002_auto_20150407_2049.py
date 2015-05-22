# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.PositiveIntegerField(verbose_name=b'Number of lesson'),
            preserve_default=True,
        ),
    ]