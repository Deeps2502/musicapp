# Generated by Django 3.2.7 on 2021-09-28 13:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dailytunes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2021, 9, 28, 13, 55, 42, 601277, tzinfo=utc)),
        ),
    ]