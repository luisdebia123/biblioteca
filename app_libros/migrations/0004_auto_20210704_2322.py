# Generated by Django 3.2.4 on 2021-07-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0003_auto_20210629_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['id'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]