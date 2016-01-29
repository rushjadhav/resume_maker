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
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name='Name')),
                ('date_of_establishment', models.DateField(null=True, verbose_name='Date of Establishment', blank=True)),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
                ('address', models.ForeignKey(related_name='address_companies', blank=True, to='profile_management.Address', null=True)),
                ('email', models.ForeignKey(related_name='email_companies', blank=True, to='profile_management.Email', null=True)),
                ('phone_number', models.ForeignKey(related_name='phone_number_companies', blank=True, to='profile_management.PhoneNumber', null=True)),
            ],
            options={
                'db_table': 'em_company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_date', models.DateField(verbose_name='From Date')),
                ('to_date', models.DateField(null=True, verbose_name='To Date ', blank=True)),
                ('designation', models.CharField(max_length=40, verbose_name='Designation')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
                ('company', models.ForeignKey(to='experience_management.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'em_experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
    ]
