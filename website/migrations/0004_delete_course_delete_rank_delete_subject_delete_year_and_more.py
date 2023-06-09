# Generated by Django 4.2 on 2023-05-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_courseevaluation_course_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Rank',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='course_title',
            field=models.CharField(choices=[('BSIT', 'Bachelor of Science in Information Technology'), ('BSIS', 'Bachelor of Science in Information Systems'), ('CompEng', 'Bachelor of Science in Computer Engineering'), ('ComScie', 'Bachelor of Science in Computer Science')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='faculty_rank',
            field=models.CharField(choices=[('Assoc Prof 1', 'Associate Professor I'), ('Assoc Prof 2', 'Associate Professor II'), ('Assoc Prof 3', 'Associate Professor III'), ('Prof 1', 'Professor I'), ('Prof 2', 'Professor II')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='subject_title',
            field=models.CharField(choices=[('DSA 1', 'Data Structure and Algorithm'), ('SAD', 'System Analysis & Design'), ('Prog I', 'Introduction to Programming')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='year',
            field=models.CharField(choices=[('Option 1', '2020'), ('Option 2', '2021'), ('Option 3', '2022'), ('Option 4', '2023'), ('Option 5', '2024'), ('Option 6', '2025')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
