# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_try', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music_info',
            old_name='releaseDate',
            new_name='releasedate',
        ),
    ]
