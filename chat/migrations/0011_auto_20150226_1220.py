# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_loginuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='loginuser',
            name='website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
