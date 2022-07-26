# Generated by Django 3.2.14 on 2022-08-06 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_number', models.CharField(max_length=100)),
                ('sne_id', models.IntegerField()),
                ('trs_area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PACSData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_number', models.IntegerField()),
                ('model_type', models.CharField(max_length=100)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipment')),
            ],
        ),
    ]
