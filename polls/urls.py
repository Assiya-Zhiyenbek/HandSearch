from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('about/', views.about, name='polls-about'),
    path('database/', views.database, name='polls-database'),
]
