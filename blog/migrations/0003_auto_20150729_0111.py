# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150729_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]
