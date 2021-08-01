from django.urls import path
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










]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
