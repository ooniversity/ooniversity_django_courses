# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant_n', to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coach_n', default=True, to='coaches.Coach'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text=b'Enter a title of course', max_length=30, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(related_name='lessons_list', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='num_in_plan',
            field=models.PositiveIntegerField(verbose_name='Number in plan'),
            preserve_default=True,
        ),
    ]
