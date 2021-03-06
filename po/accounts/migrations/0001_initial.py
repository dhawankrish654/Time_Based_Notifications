# Generated by Django 3.0.5 on 2020-05-25 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('sponsor_id', models.CharField(max_length=30)),
                ('sponsor_name', models.CharField(max_length=30)),
                ('co_sponsor_id', models.CharField(max_length=30)),
                ('co_sponsor_name', models.CharField(max_length=30)),
                ('adp_id', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=16)),
                ('dob', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=30)),
                ('father_firstname', models.CharField(max_length=50)),
                ('father_lastname', models.CharField(max_length=50)),
                ('nominee_firstname', models.CharField(max_length=50)),
                ('nominee_lastname', models.CharField(max_length=50)),
                ('nominee_gender', models.CharField(max_length=20)),
                ('nominee_dob', models.CharField(max_length=30)),
                ('relation', models.CharField(max_length=30)),
                ('pan', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('address_correspondence', models.TextField()),
                ('landmark', models.TextField()),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=30)),
                ('id_proof', models.CharField(max_length=30)),
                ('proof_address', models.TextField()),
                ('bank_name', models.CharField(max_length=30)),
                ('account_no', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=50)),
                ('ifs_code', models.CharField(max_length=30)),
                ('account_type', models.CharField(max_length=30)),
                ('success', models.IntegerField()),
                ('verify', models.IntegerField()),
                ('mobile_verify', models.IntegerField()),
                ('new_joining', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
            options={
                'db_table': 'tbl_adp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.TextField()),
                ('day', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('hrs', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
                ('min', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)])),
            ],
        ),
    ]
