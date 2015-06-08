# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20150606_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='exuserprofile',
            name='email',
            field=models.EmailField(default='vikasparasar440@gmail.com', unique=True, max_length=254),
            preserve_default=False,
        ),
    ]
