from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
#from django.db.models import Q

from Freyja import settings

# Other
import datetime
import pandas as pd
import os

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Freyja.models import AthlCompetitors, AthlAfrek

# Events

EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Freyja/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

def Print_list_vertically(my_list):
    for i in my_list:
        print(i)
    return None

# Front page
def front_page(requests):
    return render(requests, 'front_page.html')

# Get_Competitor_Info
# Looks upp information about a competitor from the AthlCompetitors table.
# Inn:
#  CompetitorCode: Fiffós ID code for the competitor
# Out:
#  Competitor_Info: A dictionary containing name, year of birth and club.
def Get_Competitor_Info(CompetitorCode):
    
    # Look upp the competitor in the table. We want an exact match.
    try:
        q = AthlCompetitors.objects.get(pk=CompetitorCode) # pk means primary key which in this case is númer
            # Make a Competitor dict with information about the competitor
        Competitor_Info = {'CompetitorCode': CompetitorCode,
                           'Name': q.nafn,
                           'FirstName': q.nafn.split(' ')[0],
                           'LastName': q.nafn.split(' ')[-1],
                           'YOB': q.fæðingarár,
                           'Club': q.félag,
                           'Datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info

def Get_List_of_Events(CompetitorCode=None):
    if (CompetitorCode == None):
        q = AthlAfrek.objects.order_by('tákn_greinar').values_list('tákn_greinar', flat=True).distinct()
    else:
        q = AthlAfrek.objects.values_list('tákn_greinar', flat=True).distinct().filter(keppandanúmer__iexact=CompetitorCode)

    Event_list = []
    for event in q:
        try:
            event_info = {'EVENT_ID': df_event_list[df_event_list['THORID_1'] == event].index[0],
                        'Name_ISL': df_event_list[df_event_list['THORID_1'] == event]['Name_ISL'].values[0],
                        'Name_ENG': df_event_list[df_event_list['THORID_1'] == event]['Name_ENG'].values[0],
                        'Name_short': df_event_list[df_event_list['THORID_1'] == event]['ShortName'].values[0],
                        'Units': df_event_list[df_event_list['THORID_1'] == event]['Units'].values[0],
                        'Wind': df_event_list[df_event_list['THORID_1'] == event]['Wind'].values[0]}
            Event_list.append(event_info)
        except:
            print('Error event not found')
            print(event)
            pass

    return Event_list


def competitor(request, CompetitorCode=None, Event=None):
    Competitor_info = Get_Competitor_Info(CompetitorCode)
    #print(Get_List_of_Events_for_Competitor(CompetitorCode))
    #Print_list_vertically(Get_List_of_Events())
    #print(Get_List_of_Events())
    Get_List_of_Events()
    return render(request, 'competitor.html', {'Competitor': Competitor_info})
