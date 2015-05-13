# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_remove_coach_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='photo',
            field=models.ImageField(upload_to=b'static/images/Coaches/', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
    ]
