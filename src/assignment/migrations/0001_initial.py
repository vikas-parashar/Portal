# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_sub', models.CharField(default=b'sub1', max_length=b'60', verbose_name=b'Main Subject', choices=[(b'sub1', b'Subject1'), (b'sub2', b'Subject2'), (b'sub3', b'Subject3')])),
                ('add_sub', models.CharField(default=b'sub1', max_length=b'60', verbose_name=b'Additional Subject', choices=[(b'sub1', b'Subject1'), (b'sub2', b'Subject2'), (b'sub3', b'Subject3')])),
                ('deadline', models.CharField(default=b'12 hours', max_length=b'60', verbose_name=b'Deadline', choices=[(b'12 hours', b'12 hours'), (b'24 hours', b'24 hours'), (b'2 days', b'2 days'), (b'3 days', b'3 days'), (b'4 days', b'4 days'), (b'5 days', b'5 days'), (b'6 days', b'6 days'), (b'1 week', b'1 week'), (b'More than 1 week', b'More than 1 week')])),
                ('details', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=b'60')),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
