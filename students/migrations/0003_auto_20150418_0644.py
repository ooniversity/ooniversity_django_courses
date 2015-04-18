# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150417_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(default=b'--------', max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
