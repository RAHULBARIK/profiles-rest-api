from django.urls import path
from profile_api import views

urlpatterns = [
    path('home-view/', views.HelloApiview.as_view()),
]
