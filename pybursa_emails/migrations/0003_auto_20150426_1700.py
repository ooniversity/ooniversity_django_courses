# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybursa_emails', '0002_auto_20150426_1024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mail',
            options={'ordering': ['-message_date']},
        ),
    ]
