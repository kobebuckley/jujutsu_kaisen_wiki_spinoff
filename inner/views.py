from django.shortcuts import render
# If there is an import error for Django Shortcuts, click and select the interpreter that says pip env

from django.http import HttpResponse


def say_hello(request): 
    return HttpResponse('HELLO THERE')