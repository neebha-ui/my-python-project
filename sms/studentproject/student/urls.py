from django.urls import path
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('add_marks/', views.add_marks, name='add_marks'),
    path('view_student/', views.view_student, name='view_student'),
    path('edit_details/<str:roll>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:roll>/', views.delete_student, name='delete_student'),

]



