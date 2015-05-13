# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0002_auto_20150423_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='mail_date',
            field=models.DateTimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043f\u0438\u0441\u044c\u043c\u0430', editable=False),
            preserve_default=True,
        ),
    ]
