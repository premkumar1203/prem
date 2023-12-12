# Generated by Django 4.2.6 on 2023-12-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='getvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probe_id', models.CharField(max_length=50, unique=True)),
                ('a_values', models.JSONField(default=list)),
                ('a1_values', models.JSONField(default=list)),
                ('b_values', models.JSONField(default=list)),
                ('b1_values', models.JSONField(default=list)),
                ('e_values', models.JSONField(default=list)),
            ],
        ),
    ]
