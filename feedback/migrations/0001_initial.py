# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mailer', models.CharField(max_length=70)),
                ('resp_email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('theme', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
