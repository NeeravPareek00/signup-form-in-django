
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sign(request):
    return render(request,"signup.html")

def thanks(request):
    return  render(request,"thanks.html")    