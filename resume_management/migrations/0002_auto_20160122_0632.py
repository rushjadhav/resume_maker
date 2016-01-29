# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='resume',
            unique_together=set([('user', 'name')]),
        ),
    ]
