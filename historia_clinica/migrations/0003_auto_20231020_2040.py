# Generated by Django 3.2.6 on 2023-10-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia_clinica', '0002_auto_20230930_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adenda',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cirugia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='condicioncronica',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
