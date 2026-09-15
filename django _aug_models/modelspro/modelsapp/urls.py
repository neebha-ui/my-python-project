from django.urls import path
from .views import student_form, student_update, student_list, student_delete

urlpatterns = [
    path('', student_form, name='student_form'),
    path('list/', student_list, name='student_list'),
    path('update/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
]

