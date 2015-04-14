# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='photo',
            field=models.FileField(upload_to=b'', null=True, verbose_name=b'Photo', blank=True),
            preserve_default=True,
        ),
    ]
