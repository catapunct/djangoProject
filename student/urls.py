from django.urls import path

from student import views

urlpatterns = [
    path('create-student/', views.StudentCreateView.as_view(), name='create_student'),
    path('list_of_students/', views.StudentsListView.as_view(), name='list-of-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-students'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('delete_student_modal/<int:pk>/', views.delete_student_modal, name='delete-student-modal'),
    path('details_student/<int:pk>/', views.StudentDetailView.as_view(), name='details-student'),
    path('student_api/', views.StudentApi.as_view(), name='student-api')
]

