# Generated by Django 4.2.17 on 2025-01-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='req',
            name='req',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
