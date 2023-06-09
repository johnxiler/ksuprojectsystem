# Generated by Django 4.2 on 2023-05-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_courseevaluation_semester_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseevaluation',
            old_name='evaluator',
            new_name='student_ID',
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='student_course',
            field=models.CharField(choices=[('BSIT', 'Bachelor of Science in Information Technology'), ('BSIS', 'Bachelor of Science in Information Systems'), ('CompEng', 'Bachelor of Science in Computer Engineering'), ('ComScie', 'Bachelor of Science in Computer Science')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseevaluation',
            name='student_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
