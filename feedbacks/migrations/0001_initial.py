# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('subject', models.CharField(max_length=55)),
                ('body', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
