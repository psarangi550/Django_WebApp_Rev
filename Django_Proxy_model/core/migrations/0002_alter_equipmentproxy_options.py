# Generated by Django 3.2.14 on 2022-08-07 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentproxy',
            options={'ordering': ('-cp_number',)},
        ),
    ]
