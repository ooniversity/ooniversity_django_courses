# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_sender', models.CharField(max_length=100, verbose_name=b'Name of sender')),
                ('subject', models.CharField(max_length=300, verbose_name=b'Theme of message')),
                ('message', models.TextField(max_length=1000, verbose_name=b'Message')),
                ('email_sender', models.EmailField(max_length=75, verbose_name=b'Email of sender')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
