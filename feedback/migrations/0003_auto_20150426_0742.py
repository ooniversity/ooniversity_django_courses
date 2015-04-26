# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_letter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='\u0412\u0430\u0448 Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letter',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='letter',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f'),
            preserve_default=True,
        ),
    ]
