from django.urls import path
from django.contrib.auth.urls import views as auth_views
from . import views


app_name = 'login'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('register/', views.register, name = "register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]