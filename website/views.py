from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'base.html'),

def contato(request):
    return render(request, 'contato.html'),