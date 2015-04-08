# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0002_auto_20150210_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tvseries',
            options={'verbose_name_plural': 'TVSeries'},
        ),
        migrations.AddField(
            model_name='tvseries',
            name='rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
