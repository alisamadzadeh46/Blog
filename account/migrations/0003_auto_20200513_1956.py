# Generated by Django 3.0.5 on 2020-05-13 15:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200513_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 15, 26, 12, 968223, tzinfo=utc), verbose_name='کاربر ویژه تا '),
        ),
    ]
