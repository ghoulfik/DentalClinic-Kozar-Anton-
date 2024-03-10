# Generated by Django 5.0.3 on 2024-03-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('num', models.CharField(max_length=13, verbose_name='Nums')),
                ('address', models.CharField(max_length=55, verbose_name='Address')),
                ('date', models.DateField()),
                ('info', models.CharField(max_length=700)),
            ],
        ),
    ]
