from django.shortcuts import render

# Create your views here.
def index(req):
  return render(req, 'index.html')


def form(req):
  return render(req, 'formulario.html')


def appvite1(req):
  return render(req, 'pagina1/index.html')

def appvite2(req):
  return render(req, 'pagina2/index.html')