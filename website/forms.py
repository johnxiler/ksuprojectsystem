from .models import CourseEvaluation  # , Rank, Course, Subject, Year
from django import forms


class CourseEvaluationForm(forms.ModelForm):
    communication = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    delivery = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    engagement = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    responsiveness = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    feedback = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    inclusiveness = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    technology = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    critical_thinking = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    motivation = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )
    satisfaction = forms.TypedChoiceField(
        choices=[(1, '1'), (2, '2'), (3, '3'),
                 (4, '4'), (5, '5')],
        widget=forms.RadioSelect(attrs={'class': 'radio-inline'}),
        coerce=int
    )

    class Meta:
        model = CourseEvaluation
        fields = ['faculty_Lname', 'faculty_Fname', 'faculty_Mname', 'faculty_rank', 'course_title', 'subject_code', 'subject_title', 'semester', 'year', 'student_ID', 'student_name', 'student_course', 'communication', 'delivery', 'engagement', 'responsiveness',
                  'feedback', 'inclusiveness', 'technology', 'critical_thinking', 'motivation', 'satisfaction', 'comments']


# class RankForm(forms.ModelForm):
#     class Meta:
#         model = Rank
#         fields = ['faculty_rank']


# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['course_title']


# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ['subject_title']


# class YearForm(forms.ModelForm):
#     class Meta:
#         model = Year
#         fields = ['year']

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['faculty_rank'].queryset = Rank.objects.all()
        #     self.fields['course_title'].queryset = Course.objects.all()
        #     self.fields['subject_title'].queryset = Subject.objects.all()
        #     self.fields['year'].choices = [
        #         (year, year) for year in range(2000, 2051)]
