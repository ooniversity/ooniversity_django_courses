# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0421\u043a\u0430\u0439\u043f', blank=True),
            preserve_default=True,
        ),
    ]
