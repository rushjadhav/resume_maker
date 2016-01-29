# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_management', '0002_auto_20160122_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(verbose_name='From Date')),
                ('to_date', models.DateField(null=True, verbose_name='To Date ', blank=True)),
                ('course_name', models.CharField(max_length=120, verbose_name='Course Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'em_education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Institude',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name='Name')),
                ('date_of_establishment', models.DateField(null=True, verbose_name='Date of Establishment', blank=True)),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
                ('address', models.ForeignKey(related_name='address_institudes', blank=True, to='profile_management.Address', null=True)),
                ('email', models.ForeignKey(related_name='email_institudes', blank=True, to='profile_management.Email', null=True)),
                ('phone_number', models.ForeignKey(related_name='phone_number_institudes', blank=True, to='profile_management.PhoneNumber', null=True)),
            ],
            options={
                'db_table': 'edum_institude',
                'verbose_name_plural': 'Institudes',
            },
        ),
        migrations.AddField(
            model_name='education',
            name='institude',
            field=models.ForeignKey(to='education_management.Institude'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
