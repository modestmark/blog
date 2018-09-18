from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sql', views.article_sql, name='article_sql'),
    path('nat', views.article_nat, name='article_nat'),
]

