# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_auto_20150413_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='coach_user',
            field=models.OneToOneField(related_name='c_user', verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
