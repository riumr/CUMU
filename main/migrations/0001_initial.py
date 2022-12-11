# Generated by Django 3.2.13 on 2022-12-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("vidid", models.CharField(default=None, max_length=130, null=True)),
                ("title", models.CharField(default=None, max_length=150, null=True)),
                ("channel", models.CharField(default=None, max_length=130, null=True)),
                (
                    "hqdefault",
                    models.CharField(default=None, max_length=130, null=True),
                ),
                ("default", models.CharField(default=None, max_length=130, null=True)),
                (
                    "mqdefault",
                    models.CharField(default=None, max_length=130, null=True),
                ),
            ],
        ),
    ]
