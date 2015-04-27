# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20150426_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='senders_email',
            new_name='your_email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='senders_name',
            new_name='your_name',
        ),
    ]
