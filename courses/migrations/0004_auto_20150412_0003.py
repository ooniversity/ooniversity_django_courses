# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150411_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assist',
            field=models.ForeignKey(related_name=b'assistant_courses', blank=b'True', to='coaches.Coach', null=b'True'),
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name=b'coach_courses', blank=b'True', to='coaches.Coach', null=b'True'),
        ),
    ]
