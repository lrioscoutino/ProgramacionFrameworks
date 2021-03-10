from django.urls import path
from apps.inicio.views import index, ViewTemplate, about, contact_us

urlpatterns = [
    path('', ViewTemplate, name='inicio'),
    path('about/', about, name='about-template'),
    path('contact-us/', contact_us, name='contact-us-template'),
]