from django.urls import path
from .views import index, form, appvite1, appvite2


urlpatterns = [
  path('', index, name="index"),
  path('form/', form, name='form'),
  path('pagina1/', appvite1, name='pagina1'),
  path('pagina2/', appvite2, name='pagina2')
]
