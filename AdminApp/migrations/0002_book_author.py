# Generated by Django 5.2.3 on 2025-07-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AdminApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(default="Unknown Author", max_length=20),
            preserve_default=False,
        ),
    ]
