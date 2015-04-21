# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailmodel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=70)),
                ('email_subject', models.CharField(max_length=70)),
                ('email_content', models.TextField(null=True, blank=True)),
                ('sender_email', models.EmailField(max_length=75, null=True, blank=True)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
