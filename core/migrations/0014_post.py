# Generated by Django 4.2.1 on 2023-06-04 20:26

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_profile_first_name_profile_second_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("user", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="post_img")),
                ("caption", models.TextField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
                ("likes", models.IntegerField(default=0)),
            ],
        ),
    ]
