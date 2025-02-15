# Generated by Django 5.1.1 on 2024-12-18 23:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokeAPP', '0016_alter_tarea_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificacion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='notificacion',
            name='tipo',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='tarea',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brokeAPP.tarea'),
        ),
    ]
