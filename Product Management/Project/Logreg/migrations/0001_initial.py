# Generated by Django 4.1.2 on 2022-10-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('Company_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Company_Name', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Itm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=30)),
                ('Item_ID', models.CharField(max_length=20)),
                ('Item_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('Product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=30)),
                ('Warranty', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=10)),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
