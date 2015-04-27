# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20150425_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmessage',
            name='message',
            field=models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
    ]
