# Generated by Django 5.0 on 2023-12-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosmiosfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name': 'Öğrenciler', 'verbose_name_plural': 'Öğrenci'},
        ),
    ]
