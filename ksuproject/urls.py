"""
URL configuration for ksuproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage, name='signup'),
    path('', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluation/<int:pk>/edit/',
         views.edit_evaluation, name='edit_evaluation'),
    path('evaluation/<int:pk>/delete/',
         views.delete_evaluation, name='delete_evaluation'),
    path('evaluation_list/',
         views.evaluation_list, name='evaluation_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/', views.student, name='student'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('account/', views.account, name='account'),
    path('add_class/', views.add_class, name='add_class'),
    path('manage_class/', views.manage_class, name='manage_class'),
    path('add_student/', views.add_student, name='add_student'),
    path('manage_student/', views.manage_student, name='manage_student'),
    path('add_questionnaire/', views.add_questionnaire,
         name='add_questionnaire'),
]
