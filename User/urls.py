from django.urls import path
from . import views
app_name = 'User'
urlpatterns = [
    path('login/', views.user_login_view.as_view()),
    path('logout/', views.user_logout_view.as_view()),
    path('', views.user_login_view.as_view()),
    path('sign-up/', views.user_adduser_view),
]


