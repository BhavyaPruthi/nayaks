# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20150228_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='votes',
            field=models.IntegerField(verbose_name='Total_votes', max_length=200),
            preserve_default=True,
        ),
    ]
