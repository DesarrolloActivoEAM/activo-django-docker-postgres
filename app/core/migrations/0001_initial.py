# Generated by Django 3.0.14 on 2021-08-02 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento_Turno',
            fields=[
                ('id_departamento_turno', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='EstatusUsuario',
            fields=[
                ('id_estatus', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id_idioma', models.AutoField(primary_key=True, serialize=False)),
                ('idioma', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id_puesto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_puesto', models.CharField(max_length=25)),
                ('departamento_turno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Departamento_Turno')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id_scope', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_scope', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Rol',
            fields=[
                ('id_tipo_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_rol', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_turno', models.CharField(max_length=25)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('p_nombre', models.CharField(max_length=25)),
                ('p_apellido', models.CharField(max_length=25)),
                ('s_apellido', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('password', models.CharField(max_length=15)),
                ('estatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.EstatusUsuario')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Idioma')),
                ('puesto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Puesto')),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Rol')),
            ],
        ),
        migrations.AddField(
            model_name='rol',
            name='scope',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Scope'),
        ),
        migrations.AddField(
            model_name='rol',
            name='tipo_rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Tipo_Rol'),
        ),
        migrations.CreateModel(
            name='Historial_Turno',
            fields=[
                ('id_historial_turno', models.AutoField(primary_key=True, serialize=False)),
                ('milisegundos', models.CharField(max_length=25)),
                ('fecha', models.DateField()),
                ('turno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Turno')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='departamento_turno',
            name='turno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Turno'),
        ),
    ]
