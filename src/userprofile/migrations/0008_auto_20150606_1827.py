# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorprofile',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
