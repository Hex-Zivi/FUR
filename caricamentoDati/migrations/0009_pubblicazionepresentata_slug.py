# Generated by Django 4.2.13 on 2024-06-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caricamentoDati', '0008_alter_relazionedocentepubblicazione_autore'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubblicazionepresentata',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
    ]
