# Generated by Django 4.1.6 on 2023-03-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('pwd', models.CharField(max_length=64)),
                ('uname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('pid', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('cid', models.CharField(max_length=4)),
                ('channel', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('unit', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('supplierid', models.PositiveIntegerField()),
                ('categoryid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
    ]
