# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20150410_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line1', models.CharField(max_length=70)),
                ('line2', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.OneToOneField(null=True, blank=True, to='students.Address'),
            preserve_default=True,
        ),
    ]
