# Generated by Django 4.2.2 on 2023-07-23 16:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("users", "0004_user_is_superuser")]

    operations = [migrations.RemoveField(model_name="user", name="username")]