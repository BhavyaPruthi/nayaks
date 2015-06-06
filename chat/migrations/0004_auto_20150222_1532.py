# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20150222_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_party',
            field=models.CharField(verbose_name='Party', default='', max_length=200),
            preserve_default=True,
        ),
    ]
