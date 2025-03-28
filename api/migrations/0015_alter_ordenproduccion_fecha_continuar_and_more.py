# Generated by Django 5.0.1 on 2025-02-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0014_alter_ordenproduccion_fecha_creacion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordenproduccion",
            name="fecha_continuar",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="ordenproduccion",
            name="fecha_creacion",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="ordenproduccion",
            name="fecha_final",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="palet",
            name="fecha_actualizacion",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="palet",
            name="fecha_creacion",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="producto",
            name="fecha_actualizacion",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="producto",
            name="fecha_creacion",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="turno",
            name="fecha_creacion",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="turno",
            name="fecha_final",
            field=models.DateTimeField(),
        ),
    ]
