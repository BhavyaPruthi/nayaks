# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20150224_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='party_type',
            field=models.CharField(max_length=100, choices=[('National Party', 'National Party'), ('state', 'State/Regional Party')], default=1),
            preserve_default=False,
        ),
    ]
