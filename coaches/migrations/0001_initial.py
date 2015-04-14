# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bdate', models.DateField()),
                ('gender', models.CharField(max_length=2, choices=[(1, b'Male'), (2, b'Famale')])),
                ('phone', models.CharField(max_length=13)),
                ('adress', models.CharField(max_length=100)),
                ('skype', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
