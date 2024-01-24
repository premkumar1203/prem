# Generated by Django 4.2.6 on 2024-01-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='constvalue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=255)),
                ('parameter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='paraname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='probecalibration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probe_id', models.CharField(max_length=50, unique=True)),
                ('low_ref', models.JSONField(default=list)),
                ('low_count', models.JSONField(default=list)),
                ('high_ref', models.JSONField(default=list)),
                ('high_count', models.JSONField(default=list)),
                ('coefficent', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='SavedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SavedParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=255)),
                ('part_model', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='serverparameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('parameter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TableFiveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TableFourData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_no', models.CharField(max_length=100)),
                ('operator_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableOneData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('part_model', models.CharField(max_length=100)),
                ('part_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableThreeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_no', models.CharField(max_length=100)),
                ('machine_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableTwoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='viewvalues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='kanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=255)),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tableonedata')),
            ],
        ),
    ]
