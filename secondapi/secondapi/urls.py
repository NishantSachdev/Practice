"""secondapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from secondapi.models import employee
from secondapi.models import department
from secondapi import views
from rest_framework.routers import DefaultRouter
from secondapi.views import org1ViewSet
from secondapi.views import org2ViewSet

router1 = DefaultRouter()
router1.register('employees', org1ViewSet, basename='employee')

router2= DefaultRouter()
router2.register('departments', org2ViewSet, basename='depart')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('org/', include(router1.urls)),
    path('org/', include(router2.urls))
]
