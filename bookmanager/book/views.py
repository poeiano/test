from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import  HttpResponse
def index(request):
    context={
        'name' : "this is a demo01"
    }
    return render(request,'book/index.html',context=context)
