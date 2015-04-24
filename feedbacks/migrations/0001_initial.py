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
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('text_message', models.TextField()),
                ('mail', models.EmailField(max_length=75)),
                ('send_data', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
