from django.urls import path,re_path
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('',views.mainV,name='main'),
    path('',views.indexV,name='index'),
    path('Business/&/Studies/',views.businessV,name='business'),
    path('login/',views.logingV,name='login'),
    path('logout/',views.loguotV,name='logout'),
    path('singup/',views.registerV,name='singup'),
    path('profile/',views.createuserV,name='profile'),
    # jquary selection
    path('selecttypeinsurance/',views.selectinsurance,name='test'),
    path('calculates/',views.calculate,name='calculate'),
    path('countrys/',views.country,name='country'),
    # End selections
    path('Business/&/Studies/save/',views.businesssaveV,name='businesssave'),
    path('Business/quatation/',views.quatationV,name='businesssaveq'),
    path('Business/addition/<int:id>',views.additionV,name='addition'),
    re_path('Business/addition/',views.additionV,name='addition'),
    path('Business/addtionsave/<int:id>',views.addtionsaveV,name='addtionsave'),
    re_path('Business/addtionsave/',views.addtionsaveV,name='addtionsave'),
    path('Business/Invoice/',views.invoiceV,name='invoice'),
    path('Business/payment/',views.paymentV,name='payment'),
    path('Business/confirmation/<int:id>',views.confirmationV,name='confirmation'),
    re_path('Business/confirmation/',views.confirmationV,name='confirmation'),
    path('Contact/Us/',views.ContactV,name='Contact'),











]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
