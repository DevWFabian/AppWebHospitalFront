# Generated by Django 4.1.1 on 2022-09-16 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0002_alter_usuario_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='user',
            new_name='credenciales',
        ),
    ]
