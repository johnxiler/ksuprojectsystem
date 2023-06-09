# Generated by Django 4.2 on 2023-05-17 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_rank', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_Lname', models.CharField(max_length=100)),
                ('faculty_Fname', models.CharField(max_length=100)),
                ('faculty_Mname', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('evaluator', models.CharField(max_length=100)),
                ('communication', models.IntegerField()),
                ('delivery', models.IntegerField()),
                ('engagement', models.IntegerField()),
                ('responsiveness', models.IntegerField()),
                ('feedback', models.IntegerField()),
                ('inclusiveness', models.IntegerField()),
                ('technology', models.IntegerField()),
                ('critical_thinking', models.IntegerField()),
                ('motivation', models.IntegerField()),
                ('satisfaction', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.course')),
                ('faculty_rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.rank')),
                ('subject_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.subject')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.year')),
            ],
        ),
    ]
