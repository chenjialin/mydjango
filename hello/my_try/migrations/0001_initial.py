# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=50)),
                ('artistLink', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('albumLink', models.CharField(max_length=200)),
                ('albumPrice', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('coverArt', models.CharField(max_length=200)),
                ('releaseDate', models.CharField(max_length=200)),
            ],
        ),
    ]
