# Generated by Django 4.1.6 on 2023-02-04 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acceso', models.CharField(default='', max_length=200, verbose_name='Acceso')),
            ],
            options={
                'verbose_name_plural': '--> Acceso',
            },
        ),
        migrations.CreateModel(
            name='SecAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.acceso')),
            ],
            options={
                'verbose_name_plural': '--> Secc_Acc',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(default='', max_length=200, verbose_name='Seccion')),
                ('accesos', models.ManyToManyField(blank=True, through='accesos.SecAcc', to='accesos.acceso')),
            ],
            options={
                'verbose_name_plural': '--> Seccion',
            },
        ),
        migrations.AddField(
            model_name='secacc',
            name='Seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.seccion'),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(default='', max_length=200, verbose_name='Area')),
                ('Seccion', models.ManyToManyField(to='accesos.seccion')),
            ],
            options={
                'verbose_name_plural': '--> Area',
            },
        ),
    ]