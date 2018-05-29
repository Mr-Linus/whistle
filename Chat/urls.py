from django.urls import path
from . import views
app_name = 'Chat'
urlpatterns = [
    path('', views.ChatView.as_view()),
    path('post/', views.post),
]


