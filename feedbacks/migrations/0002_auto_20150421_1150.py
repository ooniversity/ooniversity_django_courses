# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Feedback',
        ),
    ]
