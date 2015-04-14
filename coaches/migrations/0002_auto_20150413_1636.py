# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='user',
            field=models.OneToOneField(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
