from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.CreateGameView.as_view()),
]