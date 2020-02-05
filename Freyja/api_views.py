from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
#from django.db.models import Q

from Freyja import settings
from Freyja import data

# Other
import os

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Freyja.models import AthlCompetitors, AthlAfrek

def Print_list_vertically(my_list):
    for i in my_list:
        print(i)
    return None

def competitor(request, CompetitorCode=None, Event=None):
    Competitor_info = data.Get_Competitor_Info(CompetitorCode)
    return JsonResponse(Competitor_info, safe=False)

def events(request, Event_id=None):
    event_list = data.Get_List_of_Events(CompetitorCode=None, Event_id=Event_id)
    #print(event_list)
    return JsonResponse(event_list, safe=False)