# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='maestro',
            fields=[
                ('n_empleado', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('correo', models.EmailField(max_length=254)),
                ('categoria', models.CharField(default=b'maestros', max_length=64, null=True)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
