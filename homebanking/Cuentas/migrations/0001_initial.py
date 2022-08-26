# Generated by Django 4.1 on 2022-08-10 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('movimiento_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_de_cuenta', models.IntegerField(blank=True, null=True)),
                ('monto', models.TextField(blank=True, null=True)),
                ('tipo_de_operacion', models.TextField(blank=True, null=True)),
                ('hora', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Movimientos',
                'db_table': 'movimientos',
            },
        ),
        migrations.CreateModel(
            name='TiposDeCuenta',
            fields=[
                ('tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cuenta', models.TextField()),
            ],
            options={
                'db_table': 'tipos_de_cuenta',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cuentas.tiposdecuenta')),
            ],
            options={
                'db_table': 'cuenta',
            },
        ),
    ]