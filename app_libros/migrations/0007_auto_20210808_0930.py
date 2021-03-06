# Generated by Django 3.2.4 on 2021-08-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0006_libro_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.SmallIntegerField(default=1, verbose_name='Cantidad'),
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='libros', verbose_name='imagen'),
        ),
    ]
