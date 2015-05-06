# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coaches', '0007_auto_20150503_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name=b'User'),
            preserve_default=True,
        ),
    ]
