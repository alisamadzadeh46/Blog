# Generated by Django 3.0.5 on 2020-05-13 15:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200421_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 15, 15, 28, 424700, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
