# Generated by Django 5.0 on 2023-12-16 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items'),
        ),
    ]
