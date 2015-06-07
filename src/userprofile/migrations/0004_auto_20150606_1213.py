# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20150606_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofile',
            name='user',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
