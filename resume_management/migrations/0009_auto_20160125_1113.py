# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0008_auto_20160125_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumelanguagemap',
            name='effiency_level',
        ),
        migrations.AddField(
            model_name='resumelanguagemap',
            name='efficiency_level',
            field=models.IntegerField(default=12, verbose_name='Efficiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resumelanguagemap',
            name='resume',
            field=models.ForeignKey(related_name='resume_languages', to='resume_management.Resume'),
        ),
    ]
