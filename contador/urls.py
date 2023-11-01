from django.urls import path
from .views import index, form


urlpatterns = [
  path('', index, name="index"),
  path('form/', form, name='form')
]
