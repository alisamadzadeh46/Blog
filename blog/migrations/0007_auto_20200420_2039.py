# Generated by Django 3.0.5 on 2020-04-20 16:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200420_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.Category', verbose_name='عبارت زیر دسته'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.Category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 16, 9, 11, 676341, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
