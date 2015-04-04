# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('max_score', models.IntegerField(default=b'100', choices=[(b'50', 50), (b'100', 100), (b'200', 200), (b'300', 300)])),
                ('deadline', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
