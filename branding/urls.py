from django.urls import path, include
from branding.views import style_view

urlpatterns = [
    path('branding.css', style_view, name='styles'),
]
