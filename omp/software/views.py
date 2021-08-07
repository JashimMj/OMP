from django.shortcuts import render
from .models  import *
from django.http import JsonResponse
from django.core import serializers
from django.template.loader import render_to_string

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
    award=Awards.objects.all()
    return render(request,'pages/main.html',{'company':company,'slider':slider,
                                             'support_title':support_title,
                                             'support':support,'type':type,
                                             'typeinsurance':typeinsurance,'customer':customer,
                                             'customer_fit':customer_fit,'award':award})

def businessV(request):
    company = CompanyInformation.objects.all()
    typeinsurance = TypeOfInsurance.objects.exclude(id=1)
    classty=ClassType.objects.all()
    return render(request,'pages/business.html',{'company':company,'typeinsurance':typeinsurance,
                                                 'classty':classty})

def selectinsurance(request):
    insurance=request.GET.get('insurancetype')
    c=ClassType.objects.filter(Title=insurance).order_by('id')
    return render(request, 'select/classofinsurance.html', {'c':c})