# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0004_auto_20160122_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='status',
            field=models.CharField(default=b'A', max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')]),
        ),
    ]
