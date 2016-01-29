# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0005_auto_20160122_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='access_url',
            field=models.CharField(default=None, unique=True, max_length=120, verbose_name='Access Url'),
        ),
    ]
