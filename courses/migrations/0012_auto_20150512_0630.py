# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20150512_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.ImageField(upload_to=b'static/images/Courses/', null=True, verbose_name='\u041b\u043e\u0433\u043e', blank=True),
            preserve_default=True,
        ),
    ]
