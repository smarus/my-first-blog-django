# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 5, 17, 53, 4, 532485, tzinfo=utc)),
        ),
    ]
