# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0005_auto_20150425_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
