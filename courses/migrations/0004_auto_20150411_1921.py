# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150410_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='index',
            field=models.PositiveIntegerField(verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='topic',
            field=models.CharField(max_length=255, verbose_name='Subject'),
            preserve_default=True,
        ),
    ]
