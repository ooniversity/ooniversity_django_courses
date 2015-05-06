# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0006_auto_20150426_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=225, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='date_of_birth',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.IntegerField(default=1, max_length=1, verbose_name='\u041f\u043e\u043b', choices=[(1, b'\xd0\x9c'), (2, b'\xd0\x96')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(max_length=225, verbose_name=b'Skype'),
            preserve_default=True,
        ),
    ]
