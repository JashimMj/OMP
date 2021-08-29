from django.shortcuts import render, redirect
from .models  import *
import datetime

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

def calculate(request):
    d0 = request.GET.get('date10')
    d1 = request.GET.get('date20')
    ab1 = datetime.datetime.strptime(d0, '%Y-%m-%d')
    ab2 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    delta = ((ab2 - ab1) + datetime.timedelta(days=1))

    return render(request,'select/date.html',{'delta':delta})

def country(request):
    countrys = request.GET.get('country')
    coun = Country.objects.filter(Title=countrys).order_by('id')
    return render(request, 'select/country.html', {'coun': coun})

def quatationV(request):
    company = CompanyInformation.objects.all()
    typeinsurance = TypeOfInsurance.objects.exclude(id=1)
    users = request.user
    abc = Quatation.objects.filter(Puser=users).last()
    back=BackgroundImage.objects.filter(id=1)
    return render(request, 'pages/quatations.html', {'abc': abc,'company':company,'typeinsurance':typeinsurance,
                                                     'back':back})

def businesssaveV(request):
    if request.method == 'POST':
        cname=request.POST.get('name')
        birthdate=request.POST.get('bbirth')
        bidate=datetime.datetime.strptime(birthdate, '%Y-%m-%d')
        tinsurance=request.POST.get('typeinsurances')
        cxinsurance=request.POST.get('classinsurance')
        pson=request.POST.get('person')
        stdate=request.POST.get('stadate')
        startdate=request.POST.get('sdate')
        startdates=datetime.datetime.strptime(startdate, '%Y-%m-%d')
        enddate=request.POST.get('edate')
        enddates=datetime.datetime.strptime(enddate, '%Y-%m-%d')
        ctry=request.POST.get('country')
        tsinsurancess=TypeOfInsurance.objects.get(id=tinsurance)
        csinsurance=ClassType.objects.get(id=cxinsurance)
        cdate=datetime.datetime.now()
        custcal=(cdate-bidate).days
        customeryear=round(custcal/365)
        users=request.user
        amounts=Rate.objects.raw('select id,net as Netss,vat as Vatss,gross as Grossss from software_rate where %s >= Coustomer_Year_Start and %s <=Coustomer_Year_End and  %s >=Stay_Days_Start and %s <=Stay_Days_End and TypeInsurance_id = %s and Class_Type_id=%s',[customeryear,customeryear,stdate,stdate,tinsurance,cxinsurance])
        for amount in amounts:
            nets=amount.Netss
            vats=amount.Vatss
            Gross=amount.Grossss
            data=Quatation.objects.create(Name=cname,Date_Of_Birth=bidate,TypeInsurance=tsinsurancess,Class_Type=csinsurance,Person=pson,Sdate=startdates,Edate=enddates,
                                      Country=ctry,stadate=stdate,Puser=users,customeryear=customeryear,Net=nets,Vat=vats,Gross=Gross)
        return redirect('/Business/quatation/')


