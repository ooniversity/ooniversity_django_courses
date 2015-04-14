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
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(1, b'M'), (2, b'F')])),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('scype', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
