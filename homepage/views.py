from django.shortcuts import render
from django.http import HttpResponse

# Pycharm Test - May 18, 2022

def home(request):
    return render(request, 'home.html')


