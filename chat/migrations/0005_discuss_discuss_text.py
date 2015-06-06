# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20150222_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='discuss',
            name='discuss_text',
            field=models.CharField(verbose_name='Argument', default='', max_length=1000000),
            preserve_default=True,
        ),
    ]
