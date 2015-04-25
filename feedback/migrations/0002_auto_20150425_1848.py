# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmessage',
            name='mailer',
            field=models.CharField(max_length=70, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb5 \xd0\xb8\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedbackmessage',
            name='resp_email',
            field=models.EmailField(max_length=75, verbose_name=b'\xd0\x92\xd0\xb0\xd1\x88\xd0\xb0 \xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedbackmessage',
            name='theme',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0'),
            preserve_default=True,
        ),
    ]
