# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvseries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvseries',
            name='year',
            field=models.DateField(),
        ),
    ]
