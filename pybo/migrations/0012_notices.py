# Generated by Django 4.0.3 on 2023-12-17 05:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_question_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_title', models.CharField(max_length=100)),
                ('n_body', models.TextField()),
                ('n_hit', models.PositiveIntegerField(default=0)),
                ('n_input_date', models.DateTimeField(default=datetime.datetime(2023, 12, 17, 5, 25, 17, 370357, tzinfo=utc), verbose_name='date published')),
            ],
        ),
    ]