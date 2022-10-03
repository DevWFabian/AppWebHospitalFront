# Generated by Django 4.1.1 on 2022-09-29 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('Estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('Telefono', models.CharField(max_length=30, verbose_name='Telefono')),
                ('Genero', models.CharField(max_length=30, verbose_name='Genero')),
                ('TipoDocumento', models.CharField(max_length=30, verbose_name='TipoDocumento')),
                ('NumeroDocumento', models.CharField(max_length=30, verbose_name='NumeroDocumento')),
                ('Direccion', models.CharField(max_length=120, verbose_name='Direccion')),
                ('Ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('FechaNacimiento', models.DateField(verbose_name='FechaNacimiento')),
                ('Correo', models.EmailField(max_length=30, verbose_name='Correo')),
                ('Rol', models.CharField(max_length=30, verbose_name='Rol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
