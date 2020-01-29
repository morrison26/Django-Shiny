from django.shortcuts import render, redirect

def shiny(request):
    return render(request, 'djangoapp/shiny.html')
