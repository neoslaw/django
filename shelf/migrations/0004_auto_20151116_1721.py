# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20151114_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedition',
            name='book',
            field=models.ForeignKey(to='shelf.Book', related_name='editions'),
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(max_length=17, blank=True),
        ),
    ]
