import accounts
from . import views
#from Portal.accounts.views import dashboard
from django.urls import path,include
from django.contrib.auth import views


urlpatterns = [
    #path('login/', views.user_login, name='Login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', views.logout_then_login, name='logout-then-login'),

    #register
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    #path('teacherslist/', views.TeacherView, name='teacherslist'),
    #path('userdetail/', views.userdetail, name='userdetail'),

    #change password urls
    path('password-change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change-done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    #restore password
    path('password_reset_view/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password_reset/confirm/', views.PasswordResetConfirmView.as_view(), name='password-confirm'),
    path('password_reset/complete/', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),

    ]