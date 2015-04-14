# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150407_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_brief',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_number',
            field=models.PositiveIntegerField(unique=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf/\xd0\xbf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_theme',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
