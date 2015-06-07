# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0004_auto_20150606_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_tutor', models.CharField(default=False, max_length=b'10')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomProfile',
        ),
    ]
