# Generated by Django 4.0.3 on 2023-12-17 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0024_alter_notices_n_input_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='n_input_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 8, 52, 15, 961505, tzinfo=utc), verbose_name='date published'),
        ),
    ]
