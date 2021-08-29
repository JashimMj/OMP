from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class CompanyInformation(models.Model):
    id=models.AutoField(primary_key=True)
    Company_Name=models.CharField(max_length=255,null=True,blank=True)
    Company_Address=models.TextField(max_length=255,null=True,blank=True)
    Company_Phone_No=models.CharField(max_length=50,null=True,blank=True)
    Company_Hotline_No=models.CharField(max_length=50,null=True,blank=True)
    Company_Fax_No=models.CharField(max_length=50,null=True,blank=True)
    Company_Email_No=models.CharField(max_length=50,null=True,blank=True)
    Company_Website_No=models.CharField(max_length=50,null=True,blank=True)
    Company_Logo=models.ImageField(upload_to='logo',null=True,blank=True)
    Facebook_Link=models.CharField(max_length=200,null=True,blank=True)
    twitter_Link=models.CharField(max_length=200,null=True,blank=True)
    Linkedin_Link=models.CharField(max_length=200,null=True,blank=True)
    Instagram_Link=models.CharField(max_length=200,null=True,blank=True)
    Youtube_Link=models.CharField(max_length=200,null=True,blank=True)
    objects=models.Manager

    def __str__(self):
        return self.Company_Name

    def logo(self):
        try:
            url = self.Company_Logo.url
        except:
            url = ' '
        return url

class SliderM(models.Model):
    id=models.AutoField(primary_key=True)
    Simage=models.ImageField(null=True,blank=True)

    def image(self):
        try:
            url = self.Simage.url
        except:
            url = ' '
        return url

class SpecialSupport(models.Model):
    id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200,null=True,blank=True)
    Discription=models.TextField(max_length=200,null=True,blank=True)
    icon=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.Title

class TypeOfInsurance(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Discription = models.TextField(max_length=200, null=True, blank=True)
    icon = models.ImageField(upload_to='icon', null=True, blank=True)
    def __str__(self):
        return self.Title

    def icontype(self):
        try:
            url = self.icon.url
        except:
            url = ' '
        return url

class CustomerFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Customer_Name=models.CharField(max_length=200, null=True, blank=True)
    Discription = models.TextField(max_length=200, null=True, blank=True)
    Customer_image = models.ImageField(upload_to='icon', null=True, blank=True)

    def __str__(self):
        return self.Title

    def imagecustomer(self):
        try:
            url = self.Customer_image.url
        except:
            url = ' '
        return url


class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200, null=True, blank=True)
    Discription = models.TextField(max_length=200, null=True, blank=True)
    Award_image = models.ImageField(upload_to='icon', null=True, blank=True)

    def __str__(self):
        return self.Title

    def Awardimage(self):
        try:
            url = self.Award_image.url
        except:
            url = ' '
        return url

class ClassType(models.Model):
    id = models.AutoField(primary_key=True)
    Title=models.ForeignKey(TypeOfInsurance,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.Name


class Quatation(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,blank=True,null=True)
    Date_Of_Birth=models.DateField(blank=True,null=True)
    TypeInsurance=models.ForeignKey(TypeOfInsurance,on_delete=models.CASCADE,null=True,blank=True)
    Class_Type=models.ForeignKey(ClassType,on_delete=models.CASCADE,null=True,blank=True)
    Person=models.IntegerField(blank=True,null=True)
    Sdate=models.DateField(blank=True,null=True)
    Edate=models.DateField(blank=True,null=True)
    Country=models.CharField(max_length=255,blank=True,null=True)
    stadate=models.IntegerField(blank=True,null=True)
    Puser=models.CharField(max_length=255,blank=True,null=True)
    customeryear=models.CharField(max_length=255,blank=True,null=True)
    Net=models.IntegerField(blank=True,null=True)
    Vat=models.IntegerField(blank=True,null=True)
    Gross=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.Name


class BackgroundImage(models.Model):
    id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to='background', null=True, blank=True)


class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    TypeInsurance = models.ForeignKey(TypeOfInsurance, on_delete=models.CASCADE, null=True, blank=True)
    Class_Type = models.ForeignKey(ClassType, on_delete=models.CASCADE, null=True, blank=True)
    Coustomer_Year_Start=models.FloatField(default=True)
    Coustomer_Year_End=models.IntegerField(default=True)
    Stay_Days_Start=models.IntegerField(default=True)
    Stay_Days_End=models.IntegerField(default=True)
    net=models.IntegerField(default=True)
    Vat=models.IntegerField(default=True)
    Gross=models.IntegerField(default=True)


    def __str__(self):
        return self.TypeInsurance.Title +' ' +self.Class_Type.Name+' ' + str(self.Coustomer_Year_Start)+'-' + str(self.Coustomer_Year_End)


class AdditionalInformation(models.Model):
    id = models.AutoField(primary_key=True)
    quatation = models.ForeignKey(Quatation, on_delete=models.CASCADE, null=True, blank=True)
    Name=models.CharField(max_length=255,blank=True,null=True)
    Address=models.CharField(max_length=555,blank=True,null=True)
    Additioninfo=models.CharField(max_length=555,blank=True,null=True)
    DAddress=models.CharField(max_length=555,blank=True,null=True)
    phone=models.CharField(max_length=50,blank=True,null=True)
    Email=models.CharField(max_length=50,blank=True,null=True)
    NID=models.CharField(max_length=50,blank=True,null=True)
    pasport=models.ImageField(upload_to='passport',null=True,blank=True)
    issue=models.DateTimeField(auto_now=True)
    Bkash=models.CharField(max_length=50,blank=True,null=True)


class UserProfileM(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Present_Address=models.CharField(max_length=255,null=True,blank=True)
    Permanant_Address=models.CharField(max_length=255,null=True,blank=True)
    Image=models.ImageField(upload_to='User',null=True,blank=True)
    objects=models.Manager()

    def images(self):
        try:
            urls=self.Image.url
        except:
            urls=''
        return urls




