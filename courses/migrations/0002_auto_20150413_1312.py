# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='+', default='', to='coaches.Coach'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='+', default='', to='coaches.Coach'),
            preserve_default=False,
        ),
    ]
