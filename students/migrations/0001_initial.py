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
                ('name', models.CharField(max_length=20, verbose_name=b'Name')),
                ('surname', models.CharField(max_length=25, verbose_name=b'Surname')),
                ('birthday', models.DateField(verbose_name=b'Date of birth')),
                ('email', models.EmailField(max_length=75, verbose_name=b'E-mail')),
                ('cell', models.CharField(max_length=20, verbose_name=b'Phone number')),
                ('address', models.CharField(max_length=50, null=True, verbose_name=b'Address', blank=True)),
                ('skype', models.CharField(max_length=20, null=True, verbose_name=b'Skype', blank=True)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
