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
                ('date_of_birth', models.DateField()),
                ('sex_choices', models.CharField(max_length=15, choices=[(b'male', b'male'), (b'female', b'female')])),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
