# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materia',
            fields=[
                ('serie', models.SlugField(max_length=64, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('maestro_a', models.ForeignKey(to='app_examen.maestro')),
            ],
        ),
    ]
