# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(related_name='students', to='courses.Course'),
            preserve_default=True,
        ),
    ]
