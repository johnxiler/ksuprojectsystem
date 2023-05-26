
# from .forms import RankForm, CourseForm, SubjectForm, YearForm
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import CourseEvaluation
from .forms import CourseEvaluationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'index.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

# Create your views here.


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html', {'user': request.user})


def LogoutPage(request):
    logout(request)
    return redirect('login')


def evaluation(request):
    if request.method == 'POST':
        form = CourseEvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation_list')
    else:
        form = CourseEvaluationForm()
    return render(request, 'evaluation.html', {'form': form})


def edit_evaluation(request, pk):
    template_name = 'evaluation.html'
    success_url = reverse_lazy('evaluation_list')
    evaluation = get_object_or_404(CourseEvaluation, pk=pk)
    if request.method == 'POST':
        form = CourseEvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('evaluation_list')
    else:
        form = CourseEvaluationForm(instance=evaluation)
    return render(request, template_name, {'form': form})


def delete_evaluation(request, pk):
    template_name = 'delete_evaluation.html'
    success_url = reverse_lazy('evaluation_list')
    evaluation = get_object_or_404(CourseEvaluation, pk=pk)
    if request.method == 'POST':
        evaluation.delete()
        return redirect('evaluation_list')
    return render(request, template_name, {'evaluation_list': evaluation})


def evaluation_list(request):
    evaluations = CourseEvaluation.objects.all()
    return render(request, 'evaluation_list.html', {'evaluations': evaluations})


def dashboard(request):
    return render(request, 'index.html')


def student(request):
    return render(request, 'student.html')


def evaluate(request):
    if request.method == 'POST':
        # rank_form = RankForm(request.POST)
        # course_form = CourseForm(request.POST)
        # subject_form = SubjectForm(request.POST)
        # year_form = Year
        form = CourseEvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evaluation_list')
    else:
        # , RankForm(), CourseForm(), SubjectForm(), YearForm()
        form = CourseEvaluationForm()
    return render(request, 'evaluation.html', {'form': form, })
    # 'rank_form': rank_form, 'course_form': course_form,
    # 'subject_form': subject_form, 'year_form': year_form,


# def my_view(request):
#     rank_form = RankForm()
#     course_form = CourseForm()
#     subject_form = SubjectForm()
#     year_form = YearForm()
#     return render(request, 'evaluation.html', {
#         'rank_form': rank_form,
#         'course_form': course_form,
#         'subject_form': subject_form,
#         'year_form': year_form,
#     })
#     if request.method == 'POST':
#         rank_form = RankForm(request.POST)
#         course_form = CourseForm(request.POST)
#         subject_form = SubjectForm(request.POST)
#         year_form = Year


def account(request):
    return render(request, 'account.html')


def add_class(request):
    return render(request, 'add_class.html'),


def add_questionnaire(request):
    return render(request, 'add_questionnaire.html'),


def add_student(request):
    return render(request, 'add_student.html'),


def manage_class(request):
    return render(request, 'manage_class.html'),


def manage_student(request):
    return render(request, 'manage_student.html'),
