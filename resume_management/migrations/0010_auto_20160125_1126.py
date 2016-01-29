# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0009_auto_20160125_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumehobbymap',
            name='effiency_level',
        ),
        migrations.AddField(
            model_name='resumehobbymap',
            name='effienciency_level',
            field=models.IntegerField(default=1, verbose_name='Efficiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resumehobbymap',
            name='resume',
            field=models.ForeignKey(related_name='resume_hobbies', to='resume_management.Resume'),
        ),
    ]
