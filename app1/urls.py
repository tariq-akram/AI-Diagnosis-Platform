from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.home, name='home'),
    path('/about/',views.about, name = 'about')
]