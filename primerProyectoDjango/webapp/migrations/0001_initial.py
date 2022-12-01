# Generated by Django 4.1.3 on 2022-12-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
