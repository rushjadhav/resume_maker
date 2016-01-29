# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0003_auto_20160122_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='addresses',
            field=models.ManyToManyField(to='profile_management.Address'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='emails',
            field=models.ManyToManyField(to='profile_management.Email'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone_numbers',
            field=models.ManyToManyField(to='profile_management.PhoneNumber'),
        ),
    ]
