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
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=100)),
                ('theme', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('date_create', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
