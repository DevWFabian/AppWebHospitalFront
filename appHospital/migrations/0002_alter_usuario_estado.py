# Generated by Django 4.1.1 on 2022-09-15 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Estado',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
