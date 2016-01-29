# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_management', '0004_auto_20160122_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume_template',
            field=models.ForeignKey(related_name='template_resumes', blank=True, to='resume_management.ResumeTemplate', null=True),
        ),
    ]
