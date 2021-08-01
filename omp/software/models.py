from django.db import models

# Create your models here.

class CompanyInformation (models.Model):
    id=models.AutoField(primary_key=True)
    Company_Name=models.CharField(max_length=85,null=True,blank=True)
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
