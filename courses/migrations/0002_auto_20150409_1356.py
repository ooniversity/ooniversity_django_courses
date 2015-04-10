# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lessons',
            name='theme',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
