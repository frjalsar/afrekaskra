"""Sif URL Configuration

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
from django.urls import path, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import os

from Sif import views
from Sif import api_views

urlpatterns = [
    # Views
    #path('admin/', admin.site.urls),
    #path(r'', views.front_page, name='front_page'),
    path(r'', TemplateView.as_view(template_name='index.html')),
    #re_path(r'^keppandi/*', views.competitor, name='competitor'),
    #re_path(r'^top/*', views.top_lists, name="top_lists"),

    # API
    path(r'api/keppandi/<int:CompetitorCode>/', api_views.competitor, name ='api_competitor'),
    path(r'api/keppandi/<int:CompetitorCode>/<int:Event_id>/', api_views.competitor_event, name ='api_competitor_event'),
    path(r'api/events/', api_views.events, name ='api_events'),
    path(r'api/events/<int:Event_id>/', api_views.events, name ='api_events'),
    path(r'api/achievements/<int:CompetitorCode>/<int:Event_id>/', api_views.competitor_achievements, name='api_achievements'),
    path(r'api/top_list/<int:Event_id>/<int:IndoorOutDoor>/<int:Gender>/<int:Year>/<int:AgeStart>/<int:AgeEnd>/<int:Legal>/<int:ISL>/<int:BestByAth>/', api_views.Get_Top_100, name='api_top100'),
    path(r'api/keppandi/', api_views.competitor_list, name='api_competitor_list'),
    path(r'api/img/profile/<int:CompetitorCode>', api_views.competitor_img_profile),
    path(r'api/img/action/<int:CompetitorCode>', api_views.competitor_img_action)
]

#if 'SIF_LOCAL' in os.environ:
#    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)

#if (settings.DEBUG == True):
#    urlpatterns += static('staticfiles/', document_root='/home/kristor/FRI/Sif-site/staticfiles')
