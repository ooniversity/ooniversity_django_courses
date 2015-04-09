# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150409_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(related_name='coursekey', verbose_name='\u041a\u0443\u0440\u0441', to='courses.Course'),
            preserve_default=True,
        ),
    ]
