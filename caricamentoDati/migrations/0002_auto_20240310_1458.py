# Generated by Django 3.2.12 on 2024-03-10 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caricamentoDati', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='codiceFiscale',
            field=models.CharField(default='RSSMRA80L05F593A', max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]{6}\\d{2}[a-zA-Z]{1}\\d{2}[a-zA-Z]{1}\\d{3}[a-zA-Z]{1}$')], verbose_name='codice fiscale'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cognome_nome',
            field=models.CharField(max_length=40, verbose_name='cognome e nome'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='anno_pubblicazione',
            field=models.IntegerField(default=2024, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)], verbose_name='anno di pubblicazione'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='issn_isbn',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='issn o isbn'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='miglior_quartile',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='miglior quartile'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='num_coautori_dip',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='numero di coautori del dipartimento'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='tipologia_collezione',
            field=models.CharField(max_length=100, verbose_name='tipologia della collezione'),
        ),
        migrations.AlterField(
            model_name='pubblicazionepresentata',
            name='titolo_rivista_atti',
            field=models.CharField(max_length=200, null=True, verbose_name='titolo della rivista o atti'),
        ),
        migrations.AlterField(
            model_name='valutazione',
            name='dataCaricamento',
            field=models.DateField(blank=True, null=True, verbose_name='data di caricamento'),
        ),
    ]