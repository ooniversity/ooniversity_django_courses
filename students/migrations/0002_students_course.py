# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course',
            field=models.ManyToManyField(to='courses.Courses'),
            preserve_default=True,
        ),
    ]
