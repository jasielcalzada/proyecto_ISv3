# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0002_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='maestro_a',
            field=models.ForeignKey(related_name='maestro', to='app_examen.maestro'),
        ),
    ]
