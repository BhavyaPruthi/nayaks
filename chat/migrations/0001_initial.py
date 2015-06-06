# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('discuss_upvote', models.IntegerField(default=0)),
                ('discuss_downvote', models.IntegerField(default=0)),
                ('discuss_time', models.DateTimeField(verbose_name='speaking time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('person_name', models.CharField(max_length=200)),
                ('person_position', models.CharField(max_length=200)),
                ('person_consti', models.CharField(max_length=200)),
                ('person_count', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='discuss',
            name='person',
            field=models.ForeignKey(to='chat.Person'),
            preserve_default=True,
        ),
    ]
