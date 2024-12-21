# Generated by Django 5.1.4 on 2024-12-21 17:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0037_remove_event_accept_template_and_more"),
        ("samaware", "0001_initial"),
        ("submission", "0077_answeroption_position"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TechRider",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("text", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="authored_tech_riders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tech_riders",
                        to="event.event",
                    ),
                ),
                (
                    "submission",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tech_rider",
                        to="submission.submission",
                    ),
                ),
            ],
        ),
    ]