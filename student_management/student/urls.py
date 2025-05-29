from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/',views.home, name = 'home'),    #function base
    path('home/', views.StudentListView.as_view(), name = 'home'),
    path('create_student/',views.create_student, name = 'create_student'),
    path('edit/<int:id>/',views.update_student, name = 'update_student'),
    path('delete_student/<int:id>/',views.delete_student, name = 'delete_student'),
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.user_login, name = 'user_login'),
    path('loout/',views.user_logout, name = 'user_logout'),
]
