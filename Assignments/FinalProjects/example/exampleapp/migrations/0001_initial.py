# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('county_name', models.CharField(max_length=255)),
                ('county_slug', models.SlugField()),
                ('pop2013', models.IntegerField()),
                ('pop2012', models.IntegerField()),
                ('pop2011', models.IntegerField()),
                ('pop2010', models.IntegerField()),
                ('change', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=255)),
                ('state_slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(to='exampleapp.State'),
            preserve_default=True,
        ),
    ]
