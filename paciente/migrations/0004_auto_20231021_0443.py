# Generated by Django 2.1.5 on 2023-10-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_alter_paciente_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
