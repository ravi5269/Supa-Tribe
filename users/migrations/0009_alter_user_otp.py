# Generated by Django 4.2.3 on 2023-07-27 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0008_user_is_verified_alter_user_otp")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="otp",
            field=models.CharField(blank=True, max_length=6, null=True),
        )
    ]
