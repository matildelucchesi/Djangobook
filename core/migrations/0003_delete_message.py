# Generated by Django 4.2.1 on 2023-06-10 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Message",
        ),
    ]
