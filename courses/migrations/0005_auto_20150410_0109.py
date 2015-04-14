# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0004_auto_20150409_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistantkey', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coachkey', verbose_name='\u0422\u0440\u0435\u043d\u0435\u0440', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
