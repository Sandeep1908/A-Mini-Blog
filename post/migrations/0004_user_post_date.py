# Generated by Django 3.2.5 on 2021-08-03 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_user_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_post',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 3, 13, 15, 25, 485402)),
        ),
    ]
