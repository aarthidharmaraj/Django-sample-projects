from django.shortcuts import render
#rom django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home_addition.html',{'name':'ABCD'})

def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2

    return render(request,'dispresult.html',{'result':res})