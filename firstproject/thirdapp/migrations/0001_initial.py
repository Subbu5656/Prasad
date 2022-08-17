# Generated by Django 3.0 on 2022-08-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('gmail', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]
