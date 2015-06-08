# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_exuserprofile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exuserprofile',
            name='email',
        ),
    ]
