# Generated by Django 4.0.3 on 2022-04-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rkp', '0008_fireobject_production_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fireobject',
            name='Q_SUM',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь'),
        ),
    ]
