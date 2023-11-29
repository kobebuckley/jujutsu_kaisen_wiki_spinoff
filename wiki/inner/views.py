from django.shortcuts import render
from django.http import HttpResponse

# If there is an import error for Django Shortcuts, click and select the interpreter that says pip env




# we can pull data from a database
# transform data
# send emails etc., 

# for now we will send an HTTP Response 

def say_hello(request): 
    return HttpResponse('HELLO THERE')