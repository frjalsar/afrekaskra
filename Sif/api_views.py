from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core import serializers
#from django.db.models import Q
from django.views.decorators.cache import cache_page

from Sif import settings
from Sif import data
from Sif import records

# Other
import os
from PIL import Image

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek

def Print_list_vertically(my_list):
    for i in my_list:
        print(i)
    return None

@cache_page(60 * 15)
def competitor(request, CompetitorCode=None):
    Competitor_info = data.Get_Competitor_Info(CompetitorCode)
    Event_info = data.Get_Competitor_Events_Info(CompetitorCode)
    return JsonResponse({'Competitor': Competitor_info, 'Events': Event_info}, safe=False)

@cache_page(60 * 15)
def competitor_event(request, CompetitorCode=None, Event_id=None):
    Competitor_info = data.Get_Competitor_Info(CompetitorCode)
    Event_info, Event_data, Event_min_max_all, Event_min_max_legal, Event_progession  = data.Get_Competitor_Event(CompetitorCode, Event_id)
    #print(Event_min_max['Min'])
    return JsonResponse({'Competitor': Competitor_info,
                         'EventInfo': Event_info,
                         'EventData': Event_data,
                         'Years_all': Event_min_max_all['Years'],
                         'Max_all': Event_min_max_all['Max'],
                         'Min_all': Event_min_max_all['Min'],
                         'Tooltip_all': Event_min_max_all['Tooltip'],
                         'Years_legal': Event_min_max_legal['Years'],
                         'Max_legal': Event_min_max_legal['Max'],
                         'Min_legal': Event_min_max_legal['Min'],
                         'Tooltip_legal': Event_min_max_legal['Tooltip'],
                         'PB_dates': Event_progession['Dates'],
                         'PBs': Event_progession['PBs'],
                         'PB_tooltip': Event_progession['Tooltip']
                         },
                         safe=True)

@cache_page(60 * 15)
def competitor_list(request):
    #if request.is_ajax():
    q = request.GET.get('term', '') # Hvað notandinn sló inn í boxið
    #print('SEARCH ' + q)
    list_of_competitors = data.Get_Competitor_List(q)
    return JsonResponse(list_of_competitors, safe=False)
    #else:
    #    return HttpResponseServerError('<h1>Server Error (500)</h1>', content_type='text/html')

@cache_page(60 * 15)
def events(request, Event_id=None):
    event_list = data.Get_List_of_Events(CompetitorCode=None, Event_id=Event_id)
    #print(event_list)
    return JsonResponse(event_list, safe=False)

@cache_page(60 * 15)
def competitor_achievements(request, CompetitorCode, Event_id):
    Achievements_list = data.Get_List_of_Achievements(CompetitorCode, Event_id)
    return JsonResponse(Achievements_list, safe=False)

@cache_page(60 * 15)
def Get_Top_100(request, Event_id, IndoorOutDoor, Gender, Year, AgeStart, AgeEnd, Legal, ISL, BestByAth):
    Top_list, Event_Info = data.Top_100_List(Event_id=Event_id, Year=Year, IndoorOutDoor=IndoorOutDoor, Gender=Gender, AgeStart=AgeStart, AgeEnd=AgeEnd, Legal=Legal, ISL=ISL, BestByAth=BestByAth)
    return JsonResponse({'TopList': Top_list, 'EventInfo': Event_Info}, safe=False)

@cache_page(60 * 15)
def competitor_img_profile(request, CompetitorCode):
    filename_profile = './images/profile_{:d}.jpg'.format(CompetitorCode)
    try:
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        filename_profile = './images/profile_default.png'
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")

@cache_page(60 * 15)
def competitor_img_action(request, CompetitorCode):
    filename_action = './images/action_{:d}.jpg'.format(CompetitorCode)
    try:
        with open(filename_action, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        #return Http404()
        blank = Image.new('RGBA', (2160, 1), (255,255,255,0))
        response = HttpResponse(content_type="image/png")
        blank.save(response, "PNG")
        return response

@cache_page(60 * 15)
def competitor_records(request, CompetitorCode):
    Records = Get_Competitor_Records(CompetitorCode)
    return JsonResponse(Records, safe=False)