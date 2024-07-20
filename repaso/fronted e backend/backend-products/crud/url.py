from .views import ProductView
from django.urls import path


urlpatterns = [
    path('product/', ProductView.as_view())
]