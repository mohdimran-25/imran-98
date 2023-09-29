from django.shortcuts import render

# Create your views here.
def realme(request):
    return render(request,"realme.html")


def redmi(request):
    return render(request,"redmi.html")