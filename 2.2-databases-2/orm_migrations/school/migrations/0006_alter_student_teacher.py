# Generated by Django 3.2.13 on 2022-04-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher'),
        ),
    ]
