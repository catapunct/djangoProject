from django.urls import path

from intro import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list_of_products/', views.products, name='list-of-products'),
    path('list_of_songs/', views.songs, name='list-of-songs')
]

# PREFIXUL ESTE UNIC
# Name din path() este UNIC

