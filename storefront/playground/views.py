from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action
# not like android views (user don't see this)

def say_hello(request):
    return HttpResponse("Hello world!")
