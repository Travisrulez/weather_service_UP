# Generated by Django 3.1.5 on 2021-07-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20210108_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Password'),
        ),
    ]
