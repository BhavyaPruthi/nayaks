# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20150222_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_party',
            field=models.CharField(max_length=200, verbose_name='Party', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_consti',
            field=models.CharField(max_length=200, verbose_name='Constituency'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_count',
            field=models.IntegerField(max_length=200, verbose_name='Participation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_position',
            field=models.CharField(max_length=200, verbose_name='Post'),
            preserve_default=True,
        ),
    ]
