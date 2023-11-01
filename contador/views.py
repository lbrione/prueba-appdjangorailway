from django.shortcuts import render

# Create your views here.
def index(req):
  return render(req, 'index.html')


def form(req):
  return render(req, 'formulario.html')