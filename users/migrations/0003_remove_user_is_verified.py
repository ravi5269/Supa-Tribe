# Generated by Django 4.2.2 on 2023-07-23 15:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("users", "0002_user_is_staff_user_is_verified_user_otp")]

    operations = [migrations.RemoveField(model_name="user", name="is_verified")]
