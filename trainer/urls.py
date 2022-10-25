from django.urls import path

from trainer import views

urlpatterns = [
    path('create-trainer/', views.TrainerCreateView.as_view(), name='create_trainer'),
    path('list_of_trainers/', views.TrainerListView.as_view(), name='list-of-trainers'),
    path('update_trainer/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainers'),
    path('details_trainer/<int:pk>/', views.TrainerDetailView.as_view(), name='details-trainer')
]

