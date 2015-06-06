# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20150227_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person_count',
        ),
        migrations.AddField(
            model_name='person',
            name='votes',
            field=models.IntegerField(max_length=200, default=0, verbose_name='Total_votes'),
            preserve_default=True,
        ),
    ]
