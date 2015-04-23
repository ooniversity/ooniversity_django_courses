# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'Sender name')),
                ('subject', models.CharField(max_length=25, verbose_name=b'Theme')),
                ('message', models.TextField(null=True, verbose_name=b'Message', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('date', models.DateTimeField(verbose_name=b'Date sent', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
