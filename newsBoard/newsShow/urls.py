from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('addLike/<int:id>', views.addLike)
]
