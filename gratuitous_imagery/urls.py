from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_albums, name='all_albums'),
]

