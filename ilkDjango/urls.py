"""
URL configuration for ilkDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#bu kısımda yolunu verdiğin sayfaları ataman gerekiyor.
from django.contrib import admin
from django.urls import path
from myApp.views import*

#görseller için import ettik
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),#boş bırakırsan ana sayfa olarak atar
    path('detay/<int:id>',detay,name="detay")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
