# Generated by Django 3.2.5 on 2021-08-02 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 2, 11, 25, 50, 103348)),
        ),
    ]