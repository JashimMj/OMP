from django.db import models


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

