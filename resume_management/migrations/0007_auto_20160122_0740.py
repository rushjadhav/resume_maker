# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0006_auto_20160122_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='career_objective',
            field=models.TextField(null=True, verbose_name='Career objective', blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='access_url',
            field=models.CharField(unique=True, max_length=120, verbose_name='Access Url'),
        ),
    ]
