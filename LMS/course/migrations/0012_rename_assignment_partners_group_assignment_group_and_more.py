# Generated by Django 4.2.3 on 2023-10-25 12:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0011_rename_assignment_group_assignment_partners_assignment_partners_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignment_Partners_Group',
            new_name='Assignment_Group',
        ),
        migrations.RenameModel(
            old_name='Assignment_Partners',
            new_name='Group_Partner',
        ),
    ]