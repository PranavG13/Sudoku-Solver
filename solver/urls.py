from django.urls import path
from . import views

urlpatterns = [
    path('', views.sudoku_form, name='sudoku_form'),
]
