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
                ('name', models.CharField(help_text=b'This is name', max_length=255, verbose_name='Instructor name')),
                ('surname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=255)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
