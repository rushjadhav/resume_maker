# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0011_auto_20160125_1134'),
        ('education_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(related_name='resume_educations', default=1, to='resume_management.Resume'),
            preserve_default=False,
        ),
    ]
