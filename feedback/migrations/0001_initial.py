# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=100, verbose_name='\u0418\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('subject', models.CharField(max_length=300, verbose_name='\u0422\u0435\u043c\u0430')),
                ('senders_email', models.EmailField(max_length=75, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('message', models.TextField(max_length=1000, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created', models.DateTimeField(verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
