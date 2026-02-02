from django.urls import path
from . import views

urlpatterns = [
    path('pt-br/', views.display_portuguese_main_page, name='portuguese_main_page'),
    # path('en/', views.display_english_main_page, name='english_main_page'),
]