# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20150417_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(related_name='assistant_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_name='coach_courses', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.PositiveIntegerField(verbose_name=b'Number of lesson'),
            preserve_default=True,
        ),
    ]
