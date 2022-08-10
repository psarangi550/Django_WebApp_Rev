# Generated by Django 3.2.14 on 2022-08-09 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WFMTInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_number', models.IntegerField()),
                ('owner', models.CharField(max_length=100)),
                ('equipment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.equipment')),
            ],
        ),
    ]