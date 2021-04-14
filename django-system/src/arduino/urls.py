from django.urls import path

from .views import dashboard

app_name = 'arduino'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
