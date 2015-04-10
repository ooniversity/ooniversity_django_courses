# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_remove_coach_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name_plural': 'coaches'},
        ),
        migrations.AddField(
            model_name='coach',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
