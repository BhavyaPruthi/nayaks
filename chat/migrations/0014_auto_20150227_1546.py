# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_auto_20150227_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='website',
            field=models.CharField(max_length=100, verbose_name='Aadhar Card No.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='static/chat/images/uploaded_files', blank=True),
            preserve_default=True,
        ),
    ]
