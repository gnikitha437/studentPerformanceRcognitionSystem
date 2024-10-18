from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('students/new/', views.create_student, name='create_student'),
    path('achievements/', views.achievement_list, name='achievement-list'),
    path('achievements/new/', views.create_achievement, name='create-achievement'),
    path('logout/', auth_views.LogoutView.as_view(next_page='student-list'), name='logout'),
]