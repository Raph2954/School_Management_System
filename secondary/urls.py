from django.contrib import admin
from django.views import static
from django.urls import path, include
from secondary import views



urlpatterns = [

    path('teachers/', views.teacher_view, name='teachers'),
    #path('userdetail/', views.userdetail, name='userdetail'),
    path('students/', views.student_view, name='students'),
    path('studentdetail/', views.studentdetailview, name='studentdetail'),
    path('classes/', views.classdetail, name='classes'),

    #path('result_app/', views.ResultView, name='result_app'),

    path('settings/', views.SettingsView, name='settings'),
    #path('check_result', views.DisplayResult, name='check_result')
    path('indetail/', views.Indetail, name= 'indetail')
]
