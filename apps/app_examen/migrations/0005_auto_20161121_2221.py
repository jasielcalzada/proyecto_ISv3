# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0004_auto_20161121_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='maestro_a',
            field=models.ForeignKey(to='app_examen.maestro', max_length=64),
        ),
    ]
