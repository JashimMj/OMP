from django.shortcuts import render
from .models  import *

# Create your views here.
def indexV(request):
    return render(request,'index.html')
def mainV(request):
    company=CompanyInformation.objects.all()
    slider=SliderM.objects.all()
    return render(request,'pages/main.html',{'company':company,'slider':slider})