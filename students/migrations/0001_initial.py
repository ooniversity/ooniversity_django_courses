# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=150)),
                ('surname', models.CharField(max_length=150)),
                ('second_name', models.CharField(max_length=150)),
                ('birdth_date', models.DateTimeField()),
                ('adress', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=75)),
                ('skype', models.CharField(max_length=150)),
                ('prakt_count', models.DecimalField(max_digits=2, decimal_places=0)),
                ('kontr_count', models.DecimalField(max_digits=2, decimal_places=0)),
                ('average_score', models.DecimalField(max_digits=2, decimal_places=0)),
                ('rank', models.DecimalField(max_digits=2, decimal_places=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
