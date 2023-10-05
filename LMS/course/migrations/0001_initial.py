# Generated by Django 4.2.4 on 2023-10-04 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignment",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("due_date", models.DateTimeField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_team_submission_allowed", models.BooleanField(default=False)),
                ("Number_of_members", models.IntegerField(default=None)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                ("marks", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.category",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("is_active", models.BooleanField(default=False)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "course_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="course_images/"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("category", models.ManyToManyField(to="course.category")),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Module",
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
                ("title", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("is_active", models.BooleanField(default=False)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("course", "title")},
            },
        ),
        migrations.CreateModel(
            name="Unit",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.module"
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="unit_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("module", "title")},
            },
        ),
        migrations.CreateModel(
            name="Enrollment",
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
                ("enrollment_start_date", models.DateTimeField()),
                ("enrollment_end_date", models.DateTimeField()),
                ("is_active", models.BooleanField(default=False)),
                ("course", models.ManyToManyField(to="course.course")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enrolled_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assignment_Submission",
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
                ("submission_date", models.DateTimeField(auto_now=True)),
                ("content", models.FileField(upload_to="content/")),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.assignment",
                    ),
                ),
                (
                    "submitted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignment_submission_done_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assignment_Partners_Group",
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
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.assignment",
                    ),
                ),
                (
                    "submitted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignment_submitted_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assignment_Partners",
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
                    "assignment_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.assignment_partners_group",
                    ),
                ),
                (
                    "partners",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="partner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assignment_Grading",
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
                ("marks", models.CharField(max_length=3)),
                ("grading_datetime", models.DateTimeField(auto_now=True)),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pass", "PASS"),
                            ("fail", "FAIL"),
                            ("pending", "PENDING"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "assignment_submission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.assignment_submission",
                    ),
                ),
                (
                    "grader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignment_grader",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assignment_doer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assignment",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.unit"
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="updated_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assignment_updated_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="Video",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.URLField()),
                ("video", models.FileField(blank=True, null=True, upload_to="videos/")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.unit"
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("unit", "title")},
            },
        ),
        migrations.CreateModel(
            name="File",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.URLField()),
                ("file", models.FileField(blank=True, null=True, upload_to="Files/")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("is_updated", models.BooleanField(default=False)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_delete", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(auto_now=True)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.unit"
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("unit", "title")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="assignment",
            unique_together={("unit", "title")},
        ),
    ]
