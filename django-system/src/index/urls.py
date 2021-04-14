from django.urls import path

from .views import Index, ContactUs

app_name = 'index'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]
