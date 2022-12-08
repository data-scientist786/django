from django.urls import path
from .views import Homepage
urlpatterns = [
    path('',Homepage.as_view(),name="home")
]
