# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_brief',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_course',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_description',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_number',
            field=models.PositiveIntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf/\xd0\xbf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_theme',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xb0'),
            preserve_default=True,
        ),
    ]
