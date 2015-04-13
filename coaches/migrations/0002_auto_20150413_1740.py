# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name_plural': 'coaches'},
        ),
        migrations.AlterField(
            model_name='coach',
            name='address',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(unique=True, max_length=18),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='skype',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
