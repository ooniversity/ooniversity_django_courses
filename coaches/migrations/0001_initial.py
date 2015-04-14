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
                ('birth', models.DateField(verbose_name=b'Birthday')),
                ('sex', models.CharField(max_length=2, verbose_name=b'Sex', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(unique=True, max_length=12, verbose_name='Phone number')),
                ('address', models.CharField(help_text=b'Enter your address', max_length=256, verbose_name=b'Address')),
                ('skype', models.CharField(max_length=128, verbose_name=b'Skype')),
                ('descr', models.TextField(verbose_name=b'Description')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
