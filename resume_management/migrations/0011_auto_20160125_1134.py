# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0010_auto_20160125_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumehobbymap',
            old_name='effienciency_level',
            new_name='efficiency_level',
        ),
    ]
