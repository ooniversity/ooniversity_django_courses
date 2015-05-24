# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20150522_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u0412\u0430\u0448\u0435 \u0438\u043c\u044f')),
                ('surname', models.CharField(max_length=30, verbose_name='\u0412\u0430\u0448\u0430 \u0444\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('phone', models.CharField(max_length=15, verbose_name=b'Phone number')),
                ('mail_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0438 \u0434\u0430\u0442\u0430 \u0437\u0430\u044f\u0432\u043a\u0438')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
