# Generated by Django 4.2.5 on 2023-09-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('Kind', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('num', models.IntegerField(max_length=10)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('score', models.IntegerField(max_length=10)),
            ],
        ),
    ]
