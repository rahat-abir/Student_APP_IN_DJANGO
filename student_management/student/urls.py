from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('create_student/',views.create_student, name = 'create_student'),
    path('edit/<int:id>/',views.update_student, name = 'update_student'),
    path('delete_student/<int:id>/',views.delete_student, name = 'delete_student'),
]
