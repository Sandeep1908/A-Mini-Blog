# Generated by Django 3.2.5 on 2021-08-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_user_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='date',
            field=models.DateField(),
        ),
    ]