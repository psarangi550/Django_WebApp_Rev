# Generated by Django 3.2.14 on 2022-07-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_number', models.CharField(max_length=100)),
                ('sne_id', models.IntegerField()),
                ('trs_area', models.CharField(max_length=100)),
            ],
        ),
    ]
