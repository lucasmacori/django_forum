# Generated by Django 2.1.7 on 2019-03-10 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 10, 21, 21, 21, 801670)),
        ),
    ]
