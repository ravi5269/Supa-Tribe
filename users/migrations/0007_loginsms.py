# Generated by Django 4.2.2 on 2023-07-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_delete_userloginsms"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoginSms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
            ],
        ),
    ]