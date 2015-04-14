# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('surname', models.CharField(max_length=70)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=80)),
                ('skype', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
