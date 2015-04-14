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
                ('coach_birth', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('coach_sex', models.CharField(default=b'MAN', max_length=3, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'MAN', b'man'), (b'WOM', b'woman')])),
                ('coach_phone', models.CharField(max_length=20, null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('coach_addr', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True)),
                ('coach_skype', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9b\xd0\xbe\xd0\xb3\xd0\xb8\xd0\xbd Skype', blank=True)),
                ('coach_description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('coach_user', models.OneToOneField(verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
