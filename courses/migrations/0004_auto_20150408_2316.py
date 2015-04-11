# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150407_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_description',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_number',
            field=models.PositiveIntegerField(null=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf/\xd0\xbf', blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set([('lesson_number', 'lesson_course')]),
        ),
    ]
