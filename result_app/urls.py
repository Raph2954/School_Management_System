from django.urls import path
from result_app import views


urlpatterns = [
    path('add_result/', views.ResultView, name='add_result'),
    path('result_success/', views.ResultsuccessView, name='result_success')
]