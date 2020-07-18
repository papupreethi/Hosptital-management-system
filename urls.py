"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index1, name='home'),
    path('about/', About,name='about'),
    
    path('index1/', index1,name='index1'),
    path('admin_login/', admin_login,name='admin_login'),
    path('logout/', Logout_admin,name='logout'),
   
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)', delete_doctor, name='delete_doctor'),
    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/', add_patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)', delete_patient, name='delete_patient'),
    path('view_appointment/', view_appointment, name='view_appointment'),
    path('add_appointment/', add_appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)', delete_appointment, name='delete_appointment'),

]
