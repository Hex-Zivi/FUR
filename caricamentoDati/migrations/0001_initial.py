# Generated by Django 3.2.12 on 2024-03-10 14:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('codiceFiscale', models.CharField(default='RSSMRA80L05F593A', max_length=16, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]{6}\\d{2}[a-zA-Z]{1}\\d{2}[a-zA-Z]{1}\\d{3}[a-zA-Z]{1}$')])),
                ('cognome_nome', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Docenti',
            },
        ),
        migrations.CreateModel(
            name='PubblicazionePresentata',
            fields=[
                ('handle', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('issn_isbn', models.CharField(blank=True, max_length=30, null=True)),
                ('anno_pubblicazione', models.IntegerField(default=2024, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('doi', models.CharField(blank=True, max_length=30, null=True)),
                ('titolo', models.CharField(max_length=200)),
                ('tipologia_collezione', models.CharField(max_length=100)),
                ('titolo_rivista_atti', models.CharField(max_length=200, null=True)),
                ('indicizzato_scopus', models.BooleanField(default=False)),
                ('miglior_quartile', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('num_coautori_dip', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name_plural': 'Pubblicazioni Presentate',
            },
        ),
        migrations.CreateModel(
            name='RivistaEccellente',
            fields=[
                ('isbn', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Riviste Eccellenti',
            },
        ),
        migrations.CreateModel(
            name='Valutazione',
            fields=[
                ('nome', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('anno', models.IntegerField(default=2024, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('dataCaricamento', models.DateField(blank=True, null=True)),
                ('valore', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Valutazioni',
            },
        ),
        migrations.CreateModel(
            name='RelazioneDocentePubblicazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scelta', models.IntegerField(blank=True, default=0, null=True)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caricamentoDati.docente')),
                ('pubblicazione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caricamentoDati.pubblicazionepresentata')),
            ],
            options={
                'verbose_name_plural': 'Relazioni Docente-Pubblicazione',
            },
        ),
        migrations.AddField(
            model_name='pubblicazionepresentata',
            name='valutazione',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caricamentoDati.valutazione'),
        ),
    ]