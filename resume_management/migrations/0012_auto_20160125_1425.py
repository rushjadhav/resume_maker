# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0011_auto_20160125_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='is_pubilshed',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(default=b'A', max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')]),
        ),
    ]
