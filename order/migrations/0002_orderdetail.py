# Generated by Django 4.1.6 on 2023-03-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
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
    ]
