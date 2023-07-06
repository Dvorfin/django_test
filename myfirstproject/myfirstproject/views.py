from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')


def home(request):
    #return HttpResponse('<h1>This is home page</h1>')
    return render(request, 'home.html', {'greeting':'Hello!'})