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
                ('birthday', models.DateField(verbose_name=b'Date of birth')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('cell', models.CharField(max_length=20, verbose_name=b'Phone number')),
                ('address', models.CharField(max_length=50, null=True, verbose_name=b'Address', blank=True)),
                ('skype', models.CharField(max_length=50, null=True, verbose_name=b'Skype', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'About coach', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
