# Generated by Django 5.0.1 on 2024-02-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_ordenproduccion_lote_completo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordenproduccion",
            name="inicio_contador",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ordenproduccion",
            name="sscc_inicio",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
