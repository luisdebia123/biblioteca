# Generated by Django 3.2.4 on 2021-07-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_libros', '0005_auto_20210725_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
