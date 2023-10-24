from django.shortcuts import render

# Create your views here.


def salomlash(request):
    return render(request, 'index.html')