# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_count',
            field=models.IntegerField(default=0, max_length=200, verbose_name='Participation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_party',
            field=models.ForeignKey(to='chat.Party'),
            preserve_default=True,
        ),
    ]
