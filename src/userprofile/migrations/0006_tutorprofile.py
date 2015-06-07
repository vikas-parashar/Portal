# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20150606_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=b'60')),
                ('phone_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^[789]\\d{9}$', message=b"Phone number must be entered in the format: '999999999'.")])),
                ('subject', models.CharField(default=b'sub1', max_length=b'4', choices=[(b'sub1', b'Subject1'), (b'sub2', b'Subject2'), (b'sub3', b'Subject3')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
