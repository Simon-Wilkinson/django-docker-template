from django.urls import path
from .views import getHello

urlpatterns = [
    path('', getHello),
]
