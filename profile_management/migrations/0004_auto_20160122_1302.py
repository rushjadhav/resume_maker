# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0003_auto_20160122_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address3',
            field=models.CharField(max_length=40, null=True, verbose_name='Address3', blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.CharField(default='test', max_length=40, verbose_name='Address1'),
            preserve_default=False,
        ),
    ]
