# Generated by Django 5.1 on 2024-08-29 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_alter_item_id_alter_provider_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=144)),
                ('enlaces', models.URLField(blank=True, null=True)),
                ('localidad', models.CharField(choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Autónoma de Buenos Aires'), ('X', 'Córdoba'), ('W', 'Corrientes'), ('E', 'Entre Ríos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuquén'), ('R', 'Río Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'), ('T', 'Tucumán')], max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('localidad', models.CharField(choices=[('B', 'Buenos Aires'), ('K', 'Catamarca'), ('H', 'Chaco'), ('U', 'Chubut'), ('C', 'Ciudad Autónoma de Buenos Aires'), ('X', 'Córdoba'), ('W', 'Corrientes'), ('E', 'Entre Ríos'), ('P', 'Formosa'), ('Y', 'Jujuy'), ('L', 'La Pampa'), ('F', 'La Rioja'), ('M', 'Mendoza'), ('N', 'Misiones'), ('Q', 'Neuquén'), ('R', 'Río Negro'), ('A', 'Salta'), ('J', 'San Juan'), ('D', 'San Luis'), ('Z', 'Santa Cruz'), ('S', 'Santa Fe'), ('G', 'Santiago del Estero'), ('V', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'), ('T', 'Tucumán')], max_length=100)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.perfilempresa')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('favoritos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.favorito')),
                ('perfil_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.perfilempresa')),
                ('perfil_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.perfilusuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]