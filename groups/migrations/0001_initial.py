# Generated by Django 4.2.2 on 2023-07-23 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated_at"),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_index=True, max_length=50, verbose_name="name"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=50,
                        verbose_name="description",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="members", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "mods",
                    models.ManyToManyField(
                        related_name="mods", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        )
    ]
