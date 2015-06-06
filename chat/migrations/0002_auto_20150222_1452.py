# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_count',
            field=models.IntegerField(max_length=200),
            preserve_default=True,
        ),
    ]
