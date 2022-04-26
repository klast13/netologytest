# Generated by Django 3.2.13 on 2022-04-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementsInSensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurements',
            field=models.ManyToManyField(related_name='sensors', to='measurement.Measurement'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
