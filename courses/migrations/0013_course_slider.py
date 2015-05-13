# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20150512_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slider',
            field=models.ImageField(upload_to=b'static/images/Courses/', null=True, verbose_name='\u0421\u043b\u0430\u0439\u0434\u0435\u0440', blank=True),
            preserve_default=True,
        ),
    ]
