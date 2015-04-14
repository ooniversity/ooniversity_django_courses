# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Person Name, max length is 70 letters', max_length=70)),
                ('position', models.CharField(max_length=20, choices=[(b'student', b'Student'), (b'laborant', b'Laborant')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='student',
            name='position',
            field=models.ForeignKey(to='students.Position'),
        ),
    ]
