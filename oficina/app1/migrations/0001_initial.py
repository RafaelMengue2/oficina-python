# Generated by Django 4.2.6 on 2023-12-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('placa', models.CharField(max_length=255)),
                ('dono', models.CharField(max_length=255)),
                ('defeito', models.TextField()),
            ],
        ),
    ]
