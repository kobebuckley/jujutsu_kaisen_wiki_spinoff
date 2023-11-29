from django.urls import path
from . import views

# adding another url config than just the original in main folder

urlpatterns = [
    path('hello/', views.say_hello)
]