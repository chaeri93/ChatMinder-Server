# Generated by Django 3.0.8 on 2021-12-30 20:26

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='kakao_id',
            field=models.IntegerField(unique=True),
        ),
    ]