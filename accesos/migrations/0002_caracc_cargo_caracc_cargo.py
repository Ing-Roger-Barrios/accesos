# Generated by Django 4.1.6 on 2023-02-06 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accesos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarAcc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.acceso')),
            ],
            options={
                'verbose_name_plural': '--> Secc_Acc',
            },
        ),
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(default='', max_length=200, verbose_name='Cargo')),
                ('accesos', models.ManyToManyField(blank=True, through='accesos.CarAcc', to='accesos.acceso')),
            ],
        ),
        migrations.AddField(
            model_name='caracc',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesos.cargo'),
        ),
    ]
