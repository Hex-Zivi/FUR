# Generated by Django 3.2.12 on 2024-04-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caricamentoDati', '0011_auto_20240429_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rivistaeccellente',
            name='isbn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]