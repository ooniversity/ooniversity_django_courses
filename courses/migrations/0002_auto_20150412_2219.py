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
            field=models.ForeignKey(related_name='assistant', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(related_name='coach', verbose_name='\u0422\u0440\u0435\u043d\u0435\u0440', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='short_descript',
            field=models.CharField(max_length=255, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(verbose_name='\u041a\u0443\u0440\u0441', to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.PositiveIntegerField(verbose_name='\u2116 \u0443\u0440\u043e\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(max_length=200, verbose_name='\u0422\u0435\u043c\u0430'),
            preserve_default=True,
        ),
    ]
