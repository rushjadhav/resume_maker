# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0007_auto_20160122_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumeskillmap',
            name='effiency_level',
        ),
        migrations.AddField(
            model_name='resumeskillmap',
            name='efficiency_level',
            field=models.IntegerField(default=10, verbose_name='Efficiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
