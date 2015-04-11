# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0003_auto_20150411_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(related_name='+', default=1, to='coaches.Coach'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_name='+', to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
