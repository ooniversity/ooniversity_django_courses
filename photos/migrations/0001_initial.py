# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discription', models.CharField(max_length=60, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0444\u043e\u0442\u043e', blank=True)),
                ('photo', models.ImageField(upload_to=b'static/images/Photos/', verbose_name='\u0424\u043e\u0442\u043e')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
