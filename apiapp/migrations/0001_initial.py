# Generated by Django 4.1.5 on 2023-09-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100)),
                ('created_at', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
