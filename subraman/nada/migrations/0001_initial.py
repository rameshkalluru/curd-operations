# Generated by Django 4.0.2 on 2022-02-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ramya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
