# Generated by Django 3.0.5 on 2020-08-02 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200620_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 18, 53, 31, 796383, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
