# Generated by Django 4.2.4 on 2023-09-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_team_created_at_team_created_by_team_is_deleted_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
