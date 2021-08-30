# Generated by Django 3.2.4 on 2021-08-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0008_auto_20210818_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]