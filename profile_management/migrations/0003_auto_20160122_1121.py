# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0002_auto_20160122_0639'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='location',
            name='state',
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='location',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
