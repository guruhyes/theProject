# Generated by Django 3.1.4 on 2020-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agama',
            fields=[
                ('kode_agama', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('agama', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
