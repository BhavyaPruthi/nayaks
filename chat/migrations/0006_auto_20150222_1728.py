# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_discuss_discuss_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=1000000, default='', verbose_name='Argument')),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('time', models.DateTimeField(verbose_name='speaking time')),
                ('person', models.ForeignKey(to='chat.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='discuss',
            name='person',
        ),
        migrations.DeleteModel(
            name='Discuss',
        ),
    ]
