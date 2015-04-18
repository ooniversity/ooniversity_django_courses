# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(max_length=255, unique=True, null=True, verbose_name='\u0421\u043a\u0430\u0439\u043f', blank=True),
            preserve_default=True,
        ),
    ]
