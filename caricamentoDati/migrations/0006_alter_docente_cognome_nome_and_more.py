# Generated by Django 4.2.13 on 2024-06-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caricamentoDati', '0005_alter_pubblicazionepresentata_titolo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='cognome_nome',
            field=models.CharField(max_length=100, verbose_name='cognome e nome'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='tipologia_collezione',
            field=models.CharField(max_length=500, verbose_name='tipologia della collezione'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='titolo_rivista_atti',
            field=models.CharField(max_length=500, null=True, verbose_name='titolo della rivista o atti'),
        ),
    ]
