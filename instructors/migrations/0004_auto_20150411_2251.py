# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_auto_20150411_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='date_of_birthday_ahaha',
            new_name='date_of_birthday',
        ),
        migrations.AddField(
            model_name='instructor',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='edited_date',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='gender',
            field=models.IntegerField(default=1, choices=[(b'1', b'Male'), (b'2', b'Female')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='sulary',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(help_text=b'This is name description', max_length=255, verbose_name='Instructor Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='phone',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
    ]
