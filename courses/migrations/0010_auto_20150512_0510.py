# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20150422_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='logo',
            field=models.ImageField(upload_to=b'images/Courses/', null=True, verbose_name='\u041b\u043e\u0433\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='assistent',
            field=models.ForeignKey(related_name='assistant_courses', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='discription',
            field=models.TextField(null=True, verbose_name='\u041f\u0440\u043e \u043a\u0443\u0440\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='info',
            field=models.CharField(max_length=200, null=True, verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_name='coach_courses', verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='discription',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0443\u0440\u043e\u043a\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.PositiveIntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0443\u0440\u043e\u043a\u0430'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='theme',
            field=models.CharField(max_length=40, verbose_name='\u0422\u0435\u043c\u0430 \u0443\u0440\u043e\u043a\u0430'),
            preserve_default=True,
        ),
    ]
