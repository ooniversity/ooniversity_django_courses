# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150419_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='num',
            field=models.PositiveIntegerField(help_text=b'\xd1\x83\xd1\x80\xd0\xbe\xd0\xba\xd0\xb8 \xd1\x81 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xbd\xd0\xb8\xd0\xb6\xd0\xb5 \xd1\x83\xd0\xb6\xd0\xb5 \xd1\x81\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd1\x83\xd1\x8e\xd1\x82'),
            preserve_default=True,
        ),
    ]
