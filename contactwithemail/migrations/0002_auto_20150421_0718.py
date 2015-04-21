# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactwithemail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailmodel',
            old_name='sender_name',
            new_name='name',
        ),
    ]
