# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150411_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(related_name='+', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
