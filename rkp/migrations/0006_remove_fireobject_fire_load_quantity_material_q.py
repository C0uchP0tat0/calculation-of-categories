# Generated by Django 4.0.3 on 2022-04-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rkp', '0005_alter_quantity_fire_load'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fireobject',
            name='fire_load',
        ),
        migrations.AddField(
            model_name='quantity',
            name='material_Q',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь'),
        ),
    ]
