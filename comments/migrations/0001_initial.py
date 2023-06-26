# Generated by Django 4.2.2 on 2023-06-26 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0003_alter_user_image"),
        ("posts", "0002_post_likes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.CharField(blank=True, db_index=True, max_length=50)),
                (
                    "commented_at",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.post"
                    ),
                ),
                ("likes", models.ManyToManyField(related_name="Like", to="users.user")),
                (
                    "owner",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
