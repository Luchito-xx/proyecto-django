from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls_views'),
    path('home', views.home, name=('polls views'))
]
