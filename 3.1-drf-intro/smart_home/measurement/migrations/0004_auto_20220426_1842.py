# Generated by Django 3.2.13 on 2022-04-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_auto_20220426_1624'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MeasurementsInSensors',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
