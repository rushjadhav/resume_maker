# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='Name')),
                ('is_pubilshed', models.BooleanField(default=False, verbose_name='Share')),
                ('access_url', models.CharField(unique=True, max_length=120, verbose_name='Access Url')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='Number Of Views')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'rm_resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='ResumeHobbyMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effiency_level', models.IntegerField(verbose_name='Effiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('hobby', models.ForeignKey(to='profile_management.Hobby')),
                ('resume', models.ForeignKey(to='resume_management.Resume')),
            ],
            options={
                'db_table': 'rm_resume_hobby_map',
                'verbose_name_plural': 'Resume Hobbies',
            },
        ),
        migrations.CreateModel(
            name='ResumeLanguageMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effiency_level', models.IntegerField(verbose_name='Effiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('language', models.ForeignKey(to='profile_management.Language')),
                ('resume', models.ForeignKey(to='resume_management.Resume')),
            ],
            options={
                'db_table': 'rm_resume_language_map',
                'verbose_name_plural': 'Resume Languages',
            },
        ),
        migrations.CreateModel(
            name='ResumeSkillMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('effiency_level', models.IntegerField(verbose_name='Effiency Level', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('resume', models.ForeignKey(related_name='resume_skills', to='resume_management.Resume')),
                ('skill', models.ForeignKey(to='profile_management.Skill')),
            ],
            options={
                'db_table': 'rm_resume_skill_map',
                'verbose_name_plural': 'Resume Skills',
            },
        ),
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='Name')),
                ('code', models.CharField(unique=True, max_length=30, verbose_name='Code')),
                ('display_pic', models.ImageField(upload_to=b'', verbose_name='Display Picture')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'rm_resume_templates',
                'verbose_name_plural': 'Resume Templates',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='resume_template',
            field=models.ForeignKey(related_name='template_resumes', to='resume_management.ResumeTemplate'),
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='resumeskillmap',
            unique_together=set([('resume', 'skill')]),
        ),
        migrations.AlterUniqueTogether(
            name='resumelanguagemap',
            unique_together=set([('resume', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='resumehobbymap',
            unique_together=set([('resume', 'hobby')]),
        ),
    ]
