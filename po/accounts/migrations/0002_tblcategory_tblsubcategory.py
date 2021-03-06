# Generated by Django 3.0.5 on 2020-05-29 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'tbl_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tbl_sub_category',
                'managed': False,
            },
        ),
    ]
