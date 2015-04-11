# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150411_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='courses_assistant', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='courses_coach', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
