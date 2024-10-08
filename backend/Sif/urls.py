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
#from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic import TemplateView

import os

from Sif import views
from Sif import api_views

#handler404 = 'Sif.views.view_404'

urlpatterns = [
    # Views
    #path('admin/', admin.site.urls),
    #path(r'', views.front_page, name='front_page'),
    #path(r'', TemplateView.as_view(template_name='index.html')),
    #path(r'google04bf0be63aa8d2e2.html', TemplateView.as_view(template_name='google04bf0be63aa8d2e2.html')),
    #path(r'robots.txt', TemplateView.as_view(template_name='robots.txt')),
    #path(r'sitemap.xml', TemplateView.as_view(template_name='sitemap.xml')),
    #re_path(r'^keppandi/*', views.competitor, name='competitor'),
    #re_path(r'^top/*', views.top_lists, name="top_lists"),

    # API
    path(r'api/test/', api_views.test, name='api_test'),
    path(r'api/competitor/<int:CompetitorCode>/', api_views.get_competitor, name ='api_competitor'),
    path(r'api/competitor/<int:CompetitorCode>/<int:Event_id>/', api_views.competitor_event, name ='api_competitor_event'),
    path(r'api/competitor/<int:CompetitorCode>/<int:Event_id>/all/', api_views.competitor_event_all, name = 'api_competitor_all'),
    path(r'api/events/', api_views.events_list, name ='api_events'),
    path(r'api/events/<int:Event_id>/', api_views.events_list, name ='api_events'),
    path(r'api/achievements/<int:CompetitorCode>/<int:Event_id>/', api_views.competitor_achievements, name='api_achievements'),
    path(r'api/top_list/<int:Event_id>/<int:IndoorOutDoor>/<int:Gender>/<str:fromDate>/<str:toDate>/<int:AgeStart>/<int:AgeEnd>/<int:Legal>/<int:ISL>/<int:BestByAth>/', api_views.Get_Top_100, name='api_top100'),
    path(r'api/top_front/', api_views.Get_Top_List, name='api_top1'),
    path(r'api/competitor/', api_views.competitor_list, name='api_competitor_list'),
    path(r'api/clubs/', api_views.club_list, name='api_club_list'),
    path(r'api/img/profile/<int:CompetitorCode>/', api_views.competitor_img_profile),
    path(r'api/img/action/<int:CompetitorCode>/', api_views.competitor_img_action),
    path(r'api/img/club/<str:ClubName>/', api_views.club_logo),
    path(r'api/records/<int:CompetitorCode>/', api_views.competitor_records),
    path(r'api/records/birthdays/', api_views.record_birthdays),
    path(r'api/records/', api_views.national_records),
    path(r'api/records/masters', api_views.national_records_masters),
    path(r'api/health/', api_views.health_check),

    #re_path('[^api/*]', TemplateView.as_view(template_name='index.html')) # Senda allt sem fer ekki á API á index.html
]

#if 'SIF_LOCAL' in os.environ:
#    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)

#if (settings.DEBUG == True):
#    urlpatterns += static('staticfiles/', document_root='/home/kristor/FRI/Sif-site/staticfiles')
