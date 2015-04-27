# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_sender', models.CharField(max_length=30, verbose_name='\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c')),
                ('subject', models.CharField(max_length=100, verbose_name='\u0422\u0435\u043c\u0430')),
                ('mail_text', models.TextField(null=True, verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435', blank=True)),
                ('address_sender', models.EmailField(max_length=75, verbose_name='E-mail \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('mail_date', models.DateTimeField(default=datetime.datetime(2015, 4, 22, 10, 52, 50, 205274, tzinfo=utc), verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
