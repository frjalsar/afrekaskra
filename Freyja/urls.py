"""Freyja URL Configuration

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
#from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from Freyja import views
from Freyja import api_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'', views.front_page, name='front_page'),
    path(r'keppandi/<int:CompetitorCode>/', views.competitor, name='competitor'),
    path(r'api/keppandi/<int:CompetitorCode>/', api_views.competitor, name ='api_competitor'),
    path(r'api/events/', api_views.events, name ='api_events'),
    path(r'api/events/<int:Event_id>/', api_views.events, name ='api_events'),
    path(r'api/achievements/<int:CompetitorCode>/<int:Event_id>/', api_views.competitor_achievements, name='api_achievements'),
]
