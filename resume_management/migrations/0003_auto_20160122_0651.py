# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0002_auto_20160122_0639'),
        ('resume_management', '0002_auto_20160122_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='addresses',
            field=models.ManyToManyField(to='profile_management.Address', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='emails',
            field=models.ManyToManyField(to='profile_management.Email', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='phone_numbers',
            field=models.ManyToManyField(to='profile_management.PhoneNumber', null=True, blank=True),
        ),
    ]
