from django.shortcuts import render
from .models  import *

# Create your views here.
def indexV(request):
    return render(request,'index.html')
def mainV(request):
    company=CompanyInformation.objects.all()
    slider=SliderM.objects.all()
    support_title=SpecialSupport.objects.filter(id=1)
    support=SpecialSupport.objects.exclude(id=1)
    type=TypeOfInsurance.objects.filter(id=1)
    typeinsurance=TypeOfInsurance.objects.exclude(id=1)
    customer=CustomerFeedback.objects.filter(id=1)
    customer_fit=CustomerFeedback.objects.exclude(id=1)
    return render(request,'pages/main.html',{'company':company,'slider':slider,
                                             'support_title':support_title,
                                             'support':support,'type':type,
                                             'typeinsurance':typeinsurance,'customer':customer,
                                             'customer_fit':customer_fit})