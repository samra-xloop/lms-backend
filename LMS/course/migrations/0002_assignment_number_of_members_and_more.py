# Generated by Django 4.2.4 on 2023-10-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='assignment',
        #     name='Number_of_members',
        #     field=models.IntegerField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='assignment',
        #     name='is_team_submission_allowed',
        #     field=models.BooleanField(blank=True, null=True),
        # ),
        # migrations.AddField(
        #     model_name='assignment_submission',
        #     name='content',
        #     field=models.FileField(blank=True, null=True, upload_to='content/'),
        # ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='assignment_grading',
            name='grading_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
