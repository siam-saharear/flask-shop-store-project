# from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . import functionality_0

def index_func(response,functionality = functionality_0.random_id_generator):
    random_id = functionality()
    return HttpResponse(f"<h1>Testing for valid response on index_func. functionalities will be added later  \n{random_id}</h1>")

def dummy_home(response,functionality = functionality_0.random_id_generator):
    random_id = functionality()
    return HttpResponse(f"<h1> Testing for valid response on <i>dummy home without extra url</i>. functionalities will be added later.\n{random_id}</h1>")

def dummy_home_ex(response, functionality = functionality_0.random_id_generator):
    random_id = functionality()
    return HttpResponse(f"<h1> Testing for valid response on <i>dummy home with extra url</i>. functionalities will be added later.\n{random_id}</h1>")










