from django.urls import path
from .views import CategoriaApiView, UnaCategoriaApiView



urlpatterns = [
    path('categoria', CategoriaApiView.as_view()),
    path('categoria/<int:id>', UnaCategoriaApiView.as_view())
]