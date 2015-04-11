# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lesson_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='descriptopm',
            new_name='description',
        ),
    ]
