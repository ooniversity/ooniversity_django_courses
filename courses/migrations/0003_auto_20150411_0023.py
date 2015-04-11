# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0002_auto_20150407_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=1, to='coaches.Coach'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='info',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Short discription', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
