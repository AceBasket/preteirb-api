# Generated by Django 4.2.8 on 2023-12-07 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usages', '0002_rename_profile_usage_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='end',
            field=models.DateField(default=datetime.datetime(2023, 12, 7, 15, 45, 1, 941216, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usage',
            name='start',
            field=models.DateField(default=datetime.datetime(2023, 12, 7, 15, 45, 12, 486651, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]