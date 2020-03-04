"""root URL Configuration

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
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls import handler404
from main import views as common_views
from main.api import ModelList,ModelDetail,UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    url(r'^api/mode_list/$', ModelList.as_view(),name='Mode_list'),
    url(r'^api/auth/$', UserAuthentication.as_view(),name='Admin Authentication API'),
    url(r'^api/mode_list/(?P<model_id>\d+)$', ModelDetail.as_view(),name='Mode_list')
]

handler404 = common_views.error_404