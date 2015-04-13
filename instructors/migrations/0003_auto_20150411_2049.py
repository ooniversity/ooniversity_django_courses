# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_auto_20150411_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='date_of_birthday',
            new_name='date_of_birthday_ahaha',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Instructor Name'),
            preserve_default=True,
        ),
    ]
