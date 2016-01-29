# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import utils.validators
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_auto_20151217_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(max_length=30, null=True, verbose_name='Middle Name', blank=True)),
                ('profile_pic', models.ImageField(upload_to=b'%Y/%m/%d', null=True, verbose_name='Profile Picture', blank=True)),
                ('date_of_birth', models.DateField(verbose_name='Date of birth', validators=[utils.validators.validate_birth_date])),
                ('nationality', models.CharField(max_length=40, null=True, verbose_name='Nationality', blank=True)),
                ('status', models.CharField(default=b'A', max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_user',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address2', models.CharField(max_length=40, null=True, verbose_name='Address2', blank=True)),
                ('address1', models.CharField(max_length=40, null=True, verbose_name='Address3', blank=True)),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_hobby',
                'verbose_name_plural': 'Hobbies',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(unique=True, max_length=128, verbose_name='Phone Number')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_phone_number',
                'verbose_name_plural': 'Phone Numbers',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=120, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
            ],
            options={
                'db_table': 'pm_skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('status', models.CharField(max_length=1, verbose_name='Status', choices=[(b'A', b'Active'), (b'I', b'Inavtive')])),
                ('country', models.ForeignKey(related_name='states', verbose_name='Country', to='profile_management.Country')),
            ],
            options={
                'db_table': 'pm_state',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(related_name='locations', verbose_name='State', to='profile_management.State'),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(verbose_name='Location', to='profile_management.Location'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='addresses',
            field=models.ForeignKey(verbose_name='Addresses', blank=True, to='profile_management.Address', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emails',
            field=models.ForeignKey(verbose_name='Emails', blank=True, to='profile_management.Email', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_numbers',
            field=models.ForeignKey(verbose_name='Phone Numbers', blank=True, to='profile_management.PhoneNumber', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('name', 'state')]),
        ),
    ]
