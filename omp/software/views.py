from django.shortcuts import render, redirect
from .models  import *
import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
# Create your views here.

company = CompanyInformation.objects.all()
typeinsurance=TypeOfInsurance.objects.exclude(id=1)
def indexV(request):
    return render(request,'index.html')
def mainV(request):
    slider=SliderM.objects.all()
    support_title=SpecialSupport.objects.filter(id=1)
    support=SpecialSupport.objects.exclude(id=1)
    type=TypeOfInsurance.objects.filter(id=1)
    customer=CustomerFeedback.objects.filter(id=1)
    customer_fit=CustomerFeedback.objects.exclude(id=1)
    award=Awards.objects.all()
    return render(request,'pages/main.html',{'company':company,'slider':slider,
                                             'support_title':support_title,
                                             'support':support,'type':type,
                                             'typeinsurance':typeinsurance,'customer':customer,
                                             'customer_fit':customer_fit,'award':award})


def logingV(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request, 'User is not valid')
            return redirect('/login/')
    else:
        return render(request,'pages/login.html',{'company':company})

def loguotV(request):
    auth.logout(request)
    return redirect('/login/')

def registerV(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['cpassword']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name already taken')
                return redirect('/singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E-Mail already taken')
                return redirect('/singup/')
            else:
                users = User.objects.create_user(username=username,email=email,password=password1)
                users.save()
                info=User.objects.get(id=users.id)
                infos=UserProfileM(user=info)
                infos.save()
                messages.info(request, 'Your Registration Is Completed')
                return redirect('/login/')
        else:
            messages.info(request,'password donot match')
            return redirect('/singup/')
    else:
        return render(request,'pages/singup.html',{'company':company,'typeinsurance':typeinsurance})

@login_required(login_url='login')
def createuserV(request):
    if request.method == 'POST' and request.FILES:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present = request.POST.get('present')
        permanent = request.POST.get('permanent')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already taken')
                return redirect('/singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('/singup/')
            else:
                image = request.FILES['image']
                store = FileSystemStorage()
                filename = store.save(image.name, image)
                profile_pic_url = store.url(filename)
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                sing = UserProfileM(user=user,Phone=phone, Present_Address=present, Permanant_Address=permanent, Image=filename)
                sing.save()
                messages.info(request, 'Data Saved')
                return redirect('/create/user/')
        else:
            messages.info(request, 'password donot match')
            return redirect('/create/user/')
    else:
        return render(request,'pages/usercreate.html',{'company':company,'typeinsurance':typeinsurance})

def businessV(request):
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

@login_required(login_url='login')
def additionV(request,id=0):
    quat = Quatation.objects.get(pk=id)
    if request.method == 'POST' and request.FILES:
        names=request.POST.get('name')
        homeaddress=request.POST.get('homeaddress')
        deaddress=request.POST.get('daddress')
        addinformation=request.POST.get('ainfo')
        phones=request.POST.get('phone')
        emails=request.POST.get('email')
        nids=request.POST.get('nid')
        logo_name = request.FILES['pcopy']
        store = FileSystemStorage()
        filename = store.save(logo_name.name, logo_name)
        profile_pic_url = store.url(filename)

        data=AdditionalInformation.objects.create(quatation=quat,Name=names,Address=homeaddress,Additioninfo=addinformation,DAddress=deaddress,phone=phones,Email=emails,NID=nids,pasport=filename)
    return render(request,'pages/additionalinfo.html',{'company':company,'typeinsurance':typeinsurance,'quat':quat})

@login_required(login_url='login')
def addtionsaveV(request,id=0):
    quat = Quatation.objects.get(pk=id)
    if request.method == 'POST' and request.FILES:
        names=request.POST.get('name')
        homeaddress=request.POST.get('homeaddress')
        deaddress=request.POST.get('daddress')
        addinformation=request.POST.get('ainfo')
        phones=request.POST.get('phone')
        emails=request.POST.get('email')
        nids=request.POST.get('nid')
        logo_name = request.FILES['pcopy']
        store = FileSystemStorage()
        filename = store.save(logo_name.name, logo_name)
        profile_pic_url = store.url(filename)

        data=AdditionalInformation.objects.create(quatation=quat,Name=names,Address=homeaddress,Additioninfo=addinformation,DAddress=deaddress,phone=phones,Email=emails,NID=nids,pasport=filename)
    return redirect('/Business/Invoice/')

@login_required(login_url='login')
def invoiceV(request):
    users = request.user
    abc = AdditionalInformation.objects.filter(quatation__Puser=users).last()
    return render(request,'pages/invoice.html',{'company':company,'typeinsurance':typeinsurance,'abc':abc})


@login_required(login_url='login')
def paymentV(request):
    users = request.user
    abc = AdditionalInformation.objects.filter(quatation__Puser=users).last()
    return render(request,'pages/payment.html',{'company':company,'abc':abc,'typeinsurance':typeinsurance})

@login_required(login_url='login')
def confirmationV(request,id=0):
    if id !=0:
        bkash=request.POST.get('mobile')
        data=AdditionalInformation.objects.get(pk=id)
        data.Bkash=bkash
        data.save()

    return render(request,'pages/confarmation.html',{'company':company,'typeinsurance':typeinsurance})

def ContactV(request):
    return render(request,'pages/Contactus.html',{'company':company,'typeinsurance':typeinsurance})