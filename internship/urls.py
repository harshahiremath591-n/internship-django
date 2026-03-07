"""
URL configuration for internship project.

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
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('student_home/', views.student_home, name='student_home'),
    path('edit_student/', views.edit_student, name='edit_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('logout/', views.logout, name='logout'),
    path('contact',views.contact,name='contact'),
    path('week3_5',views.week3_5,name='week3_5'),
    path('week4_4',views.week4_4,name='week4_4'),
    path('basic',views.basic,name='basic'),
    path('s_portel',views.s_portel,name='s_portel'),
    path('js_basics',views.js_basics,name='js_basics'),
    path('mini_project',views.mini_project basics,name='mini_project'),
    path('list',views.list basics,name='list'),
]
