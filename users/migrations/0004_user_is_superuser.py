# Generated by Django 4.2.2 on 2023-07-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0003_remove_user_is_verified")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        )
    ]
