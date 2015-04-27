# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybursa_emails', '0003_auto_20150426_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='send_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mail',
            name='message_date',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
    ]
