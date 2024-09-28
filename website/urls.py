from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_form_view, name='question_form_view'),
    path('questions/', views.question_list_view, name='question_list'),
]
