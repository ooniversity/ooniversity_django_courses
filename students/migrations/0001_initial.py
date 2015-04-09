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
                ('name', models.CharField(max_length=25, verbose_name=b'Name')),
                ('surname', models.CharField(max_length=25, verbose_name=b'Surname')),
                ('birthday', models.DateField(verbose_name=b'Birthday')),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name=b'Email')),
                ('phone_num', models.CharField(unique=True, max_length=12, verbose_name=b'Phone number')),
                ('address', models.CharField(max_length=256, verbose_name=b'Address')),
                ('skype', models.CharField(max_length=128, verbose_name=b'Skype')),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
