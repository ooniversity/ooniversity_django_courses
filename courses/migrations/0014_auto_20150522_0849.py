# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_course_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('autor', models.CharField(default='\u0413\u043e\u0441\u0442\u044c', max_length=30, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('discription', models.TextField(verbose_name='\u041e\u0442\u0437\u044b\u0432')),
                ('date_public', models.DateTimeField(auto_now=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f', auto_now_add=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='finish',
            field=models.DateField(null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043a\u0443\u0440\u0441\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='start',
            field=models.DateField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u043a\u0443\u0440\u0441\u0430', blank=True),
            preserve_default=True,
        ),
    ]
