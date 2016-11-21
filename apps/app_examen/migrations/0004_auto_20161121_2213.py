# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0003_auto_20161121_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='maestro_a',
            field=models.ForeignKey(related_name='maestr', to='app_examen.maestro'),
        ),
    ]
