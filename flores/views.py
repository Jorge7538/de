from django.shortcuts import render

def carta_animada(request):
    return render(request, 'flores/index.html')                   