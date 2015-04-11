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
            name='student_addr',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birth',
            field=models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_course',
            field=models.ManyToManyField(to='courses.Course', verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=75, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81 \xd1\x8d\xd0\xbb.\xd0\xbf\xd0\xbe\xd1\x87\xd1\x82\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_last_name',
            field=models.CharField(max_length=30, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_phone',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_skype',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd Skype'),
            preserve_default=True,
        ),
    ]
