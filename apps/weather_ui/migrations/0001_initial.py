# Generated by Django 3.1.5 on 2021-01-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='50')),
                ('password', models.CharField(max_length=50, verbose_name='50')),
            ],
        ),
    ]
