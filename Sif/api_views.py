from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
from django.core import serializers
#from django.db.models import Q

from Sif import settings
from Sif import data

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

def competitor(request, CompetitorCode=None):
    Competitor_info = data.Get_Competitor_Info(CompetitorCode)
    Event_info = data.Get_Competitor_Events_Info(CompetitorCode)
    return JsonResponse({'Competitor': Competitor_info, 'Events': Event_info}, safe=False)

def competitor_event(request, CompetitorCode=None, Event_id=None):
    Competitor_info = data.Get_Competitor_Info(CompetitorCode)
    Event_info, Event_data, Event_min_max = data.Get_Competitor_Event(CompetitorCode, Event_id)
    #print(Event_min_max['Min'])
    return JsonResponse({'Competitor': Competitor_info,
                         'EventInfo': Event_info,
                         'EventData': Event_data,
                         'Years': Event_min_max['Years'],
                         'Max': Event_min_max['Max'],
                         'Min': Event_min_max['Min'],
                         'Tooltip': Event_min_max['Tooltip']
                         },
                         safe=True)

def competitor_list(request):
    #if request.is_ajax():
    q = request.GET.get('term', '') # Hvað notandinn sló inn í boxið
    #print('SEARCH ' + q)
    list_of_competitors = data.Get_Competitor_List(q)
    return JsonResponse(list_of_competitors, safe=False)
    #else:
    #    return HttpResponseServerError('<h1>Server Error (500)</h1>', content_type='text/html')

def events(request, Event_id=None):
    event_list = data.Get_List_of_Events(CompetitorCode=None, Event_id=Event_id)
    #print(event_list)
    return JsonResponse(event_list, safe=False)

def competitor_achievements(request, CompetitorCode, Event_id):
    Achievements_list = data.Get_List_of_Achievements(CompetitorCode, Event_id)
    return JsonResponse(Achievements_list, safe=False)

def Get_Top_100(request, Event_id, IndoorOutDoor, Gender, Year, AgeStart, AgeEnd, Legal, ISL, BestByAth):
    Top_list, Event_Info = data.Top_100_List(Event_id=Event_id, Year=Year, IndoorOutDoor=IndoorOutDoor, Gender=Gender, AgeStart=AgeStart, AgeEnd=AgeEnd, Legal=Legal, ISL=ISL, BestByAth=BestByAth)
    return JsonResponse({'TopList': Top_list, 'EventInfo': Event_Info}, safe=False)

def competitor_img_profile(request, CompetitorCode):
    filename_profile = './images/profile_{:d}.jpg'.format(CompetitorCode)
    try:
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        filename_profile = './images/profile_default.png'
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")

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