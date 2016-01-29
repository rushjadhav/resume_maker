# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emails',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_numbers',
        ),
    ]
