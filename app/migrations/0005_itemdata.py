# Generated by Django 4.2.6 on 2023-12-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rowdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('data', models.TextField()),
            ],
        ),
    ]
