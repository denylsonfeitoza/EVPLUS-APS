from django.urls import path
from . import views

urlpatterns = [
    path('novo-evento/', views.eventos, name='eventos'),

]