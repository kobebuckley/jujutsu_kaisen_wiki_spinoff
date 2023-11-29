from django.shortcuts import render
# If there is an import error for Django Shortcuts, click and select the interpreter that says pip env

from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate() 
    return render(request, 'hello.html', {'name': 'Kobe'})