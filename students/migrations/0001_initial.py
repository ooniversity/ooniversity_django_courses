# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=10)),
                ('date_birthday', models.DateField()),
                ('mail', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=40)),
                ('skype', models.CharField(max_length=10)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
