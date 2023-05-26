from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# class Rank(models.Model):
#     OPTIONS = (
#         ('Assoc Prof 1', 'Associate Professor I'),
#         ('Assoc Prof 2', 'Associate Professor II'),
#         ('Assoc Prof 3', 'Associate Professor III'),
#         ('Prof 1', 'Professor I'),
#         ('Prof 2', 'Professor II'),
#     )
#     faculty_rank = models.CharField(max_length=50, choices=OPTIONS)
#     # faculty_rank = models.CharField(max_length=100)

#     # def __str__(self):
#     #     return str(self.faculty_rank)


# class Course(models.Model):
#     OPTIONS = (
#         ('BSIT', 'Bachelor of Science in Information Technology'),
#         ('BSIS', 'Bachelor of Science in Information Systems'),
#         ('CompEng', 'Bachelor of Science in Computer Engineering'),
#         ('ComScie', 'Bachelor of Science in Computer Science'),
#     )
#     course_title = models.CharField(max_length=50, choices=OPTIONS)
#     # course_title = models.CharField(max_length=100)

#     # def __str__(self):
#     #     return str(self.course_title)


# class Subject(models.Model):
#     OPTIONS = (
#         ('DSA 1', 'Data Structure and Algortihm'),
#         ('SAD', 'System Analysis & Design'),
#         ('Prog I', 'Introduction to Programming'),
#     )
#     subject_title = models.CharField(max_length=50, choices=OPTIONS)
#     # subject_title = models.CharField(max_length=100)

#     # def __str__(self):
#     #     return str(self.subject_title)


# class Year(models.Model):
#     OPTIONS = (
#         ('Option 1', '2020'),
#         ('Option 2', '2021'),
#         ('Option 3', '2022'),
#         ('Option 4', '2023'),
#         ('Option 5', '2024'),
#         ('Option 6', '2025'),
#     )
#     year = models.CharField(max_length=50, choices=OPTIONS)
# year = models.CharField(max_length=100)

# def __str__(self):
#     return str(self.year)
# Create a model with a field to store the chosen option as an integer


class CourseEvaluation(models.Model):
    faculty_Lname = models.CharField(max_length=100)
    faculty_Fname = models.CharField(max_length=100)
    faculty_Mname = models.CharField(max_length=100)
    # faculty_rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    OPTIONS = (
        ('Assoc Prof 1', 'Associate Professor I'),
        ('Assoc Prof 2', 'Associate Professor II'),
        ('Assoc Prof 3', 'Associate Professor III'),
        ('Prof 1', 'Professor I'),
        ('Prof 2', 'Professor II'),
    )
    faculty_rank = models.CharField(max_length=50, choices=OPTIONS)

    # course_title = models.ForeignKey(Course, on_delete=models.CASCADE)
    OPTIONS = (
        ('BSIT', 'Bachelor of Science in Information Technology'),
        ('BSIS', 'Bachelor of Science in Information Systems'),
        ('CompEng', 'Bachelor of Science in Computer Engineering'),
        ('ComScie', 'Bachelor of Science in Computer Science'),

    )
    course_title = models.CharField(max_length=50, choices=OPTIONS)
    OPTIONS = (
        # 1st element is shown in the database while 2nd element shown in the dropdown menus.
        ('CC 118', 'CC 118'),
        ('CC 119', 'CC 119'),
        ('CC 120', 'CC 120'),
        ('CC 121', 'CC 121'),
        ('CC 122', 'CC 122'),
        ('CC 123', 'CC 123'),
        ('TECHNO  11', 'TECHNO  11'),
        ('PROF ED 14', 'PROF ED 14'),
    )
    subject_code = models.CharField(max_length=50, choices=OPTIONS)
    # subject_title = models.ForeignKey(Subject, on_delete=models.CASCADE)
    OPTIONS = (
        # 1st element is shown in the database while 2nd element shown in the dropdown menus.
        ('Information Assurance and Security 1',
         'Information Assurance and Security 1'),
        ('Social and Professional Issues', 'Social and Professional Issues'),
        ('Application Development and Emerging',
         'Application Development and Emerging'),
        ('System Integration and Architecture 1',
         'System Integration and Architecture 1'),
        ('System Integration and Architecture 1',
         'System Integration and Architecture 1'),
        ('Capstone Project and Research 1', 'Capstone Project and Research 1'),
        ('Technopreneurship', 'Technopreneurship'),
        ('Assessment of Learning 1', 'Assessment of Learning 1'),
    )
    subject_title = models.CharField(max_length=50, choices=OPTIONS)
    OPTIONS = (
        ('1st semester', '1st semester'),
        ('2nd semester', '2nd semester'),
        ('Summer Class', 'Summer Class'),
    )
    semester = models.CharField(max_length=100, choices=OPTIONS)
    # year = models.ForeignKey(Year, on_delete=models.CASCADE)
    OPTIONS = (
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
    )
    year = models.CharField(max_length=50, choices=OPTIONS)
    student_ID = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    OPTIONS = (
        ('BSIT', 'Bachelor of Science in Information Technology'),
        ('BSIS', 'Bachelor of Science in Information Systems'),
        ('CompEng', 'Bachelor of Science in Computer Engineering'),
        ('ComScie', 'Bachelor of Science in Computer Science'),
    )
    student_course = models.CharField(max_length=100, choices=OPTIONS)
    communication = models.IntegerField()
    delivery = models.IntegerField()
    engagement = models.IntegerField()
    responsiveness = models.IntegerField()
    feedback = models.IntegerField()
    inclusiveness = models.IntegerField()
    technology = models.IntegerField()
    critical_thinking = models.IntegerField()
    motivation = models.IntegerField()
    satisfaction = models.IntegerField()
    comments = models.CharField(max_length=200)

    @property
    def total_average(self):
        return sum([self.communication, self.delivery, self.engagement, self.responsiveness, self.feedback,
                    self.inclusiveness, self.technology, self.critical_thinking, self.motivation, self.satisfaction]) / 10

    def __str__(self):
        return f"{self.course_title} - {self.faculty_Lname} ({self.semester} {self.year})"

    # def clean(self):
    #     try:
    #         faculty_rank = Rank.objects.get(id=self.faculty_rank_id)
    #     except Rank.DoesNotExist:
    #         raise ValidationError('Invalid faculty rank id')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        # Save the CourseEvaluation object
