from threading import Event
from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
#from django.shortcuts import render
#from django.urls import reverse
from django.views.decorators.cache import never_cache
#from django.views.generic.base import RedirectView
#from django.core import serializers
#from django.db.models import Q
from django.views.decorators.cache import cache_page

#from Sif import settings
from Sif import data
from Sif import records
from Sif import competitor
from Sif import events

# Other
import os
import urllib
from PIL import Image
from babel.dates import format_date #, format_datetime, format_time

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek

# Health check
def health_check(request):
    return JsonResponse({'health': 'ok'}, safe=False)

def Print_list_vertically(my_list):
    for i in my_list:
        print(i)
    return None

def test(request):
    return JsonResponse({'test': 'test'}, safe=False)

@cache_page(60 * 5)
def get_competitor(request, CompetitorCode=None):
    df = competitor.Get_Competitor_Achievements(CompetitorCode)
    Competitor_info = competitor.Get_Competitor_Info(CompetitorCode)
    Event_info = competitor.Get_Competitor_Events_Info(df, CompetitorCode)
    club_list, club_history = competitor.Get_Club_By_Year(df)
    return JsonResponse({'Competitor': Competitor_info, 'Events': Event_info, 'Clubs': club_history}, safe=False)

# Skilar öllum gögnum fyrir tiltekna grein.
@cache_page(60 * 5)
def competitor_event_all(request, CompetitorCode, Event_id):
    EventData_all = data.Get_Competitor_Event_Data_All(CompetitorCode, Event_id)
    return JsonResponse(EventData_all, safe=False)

@cache_page(60 * 60 * 1)
def competitor_event(request, CompetitorCode=None, Event_id=None):
    Competitor_info = competitor.Get_Competitor_Info(CompetitorCode)
    Event_info, Event_data, Event_min_max_all, Event_min_max_legal, Event_progession  = competitor.Get_Competitor_Event(CompetitorCode, Event_id)
    #print(Event_min_max['Min'])
    return JsonResponse({'Competitor': Competitor_info,
                         'EventInfo': Event_info,
                         'EventData': Event_data,
                         'Years_all': Event_min_max_all['Years'],
                         'Max_all': Event_min_max_all['Max'],
                         'Min_all': Event_min_max_all['Min'],
                         'Tooltip_all_max': Event_min_max_all['Tooltip_max'],
                         'Tooltip_all_min': Event_min_max_all['Tooltip_min'],
                         'Years_legal': Event_min_max_legal['Years'],
                         'Max_legal': Event_min_max_legal['Max'],
                         'Min_legal': Event_min_max_legal['Min'],
                         'Tooltip_legal_max': Event_min_max_legal['Tooltip_max'],
                         'Tooltip_legal_min': Event_min_max_legal['Tooltip_min'],
                         'PB_dates': Event_progession['Dates'],
                         'PBs': Event_progession['PBs'],
                         'PB_tooltip': Event_progession['Tooltip']
                         },
                         safe=True)

@cache_page(60 * 60 * 48)
def competitor_list(request):
    s = request.GET.get('search', '') # Hvað notandinn sló inn í boxið
    club = request.GET.get('clubId', None)
    startsWith = request.GET.get('startsWith', None)
    yob = request.GET.get('yob', None)
    list_of_competitors = data.Get_Competitor_List(s, club, startsWith, yob)
    return JsonResponse(list_of_competitors, safe=False)
    #else:
    #    return HttpResponseServerError('<h1>Server Error (500)</h1>', content_type='text/html')

@cache_page(60 * 60 * 24)
def club_list(request):
    #list_of_clubs = data.Get_Club_List()
    list_of_clubs = data.Get_Club_List_Thor()
    return JsonResponse(list_of_clubs, safe=False)

@cache_page(60 * 60 * 0)
def events_list(request, Event_id=None):
    event_list = data.Get_List_of_Events(CompetitorCode=None, Event_id=Event_id)
    #print(event_list)
    return JsonResponse(event_list, safe=False)

@cache_page(60 * 60 * 0)
def competitor_achievements(request, CompetitorCode, Event_id):
    Achievements_list = data.Get_List_of_Achievements(CompetitorCode, Event_id)
    return JsonResponse(Achievements_list, safe=False)

@cache_page(60 * 60 * 0)
def Get_Top_100(request, Event_id, IndoorOutDoor, Gender, fromDate, toDate, AgeStart, AgeEnd, Legal, ISL, BestByAth):
    #print('Get_Top_100')
    Top_list, Event_Info = data.Top_100_List(Event_id=Event_id, fromDate=fromDate, toDate=toDate, IndoorOutDoor=IndoorOutDoor, Gender=Gender, AgeStart=AgeStart, AgeEnd=AgeEnd, Legal=Legal, ISL=ISL, BestByAth=BestByAth)
    return JsonResponse({'TopList': Top_list, 'EventInfo': Event_Info}, safe=False)

@cache_page(60 * 60 * 12)
def Get_Top_List(request):
    Top_list_Women, Top_list_Men = data.Top_List()
    return JsonResponse({'Women': Top_list_Women, 'Men': Top_list_Men}, safe=False)

@cache_page(60 * 60 * 24 * 7)
def competitor_img_profile(request, CompetitorCode):
    filename_profile = './images/profile_{:d}.jpg'.format(CompetitorCode)
    try:
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        filename_profile = './images/profile_default.jpg'
        with open(filename_profile, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")

    raise Http404() # Ættum ekki að koma hingað

@cache_page(60 * 60 * 24 * 7)
def competitor_img_action(request, CompetitorCode):
    #print('competitor_img_action')
    filename_action = './images/action_{:d}.jpg'.format(CompetitorCode)
    try:
        with open(filename_action, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        #raise Http404()
        #blank = Image.new('RGBA', (2160, 150), (255,255,255,0))
        #response = HttpResponse(content_type="image/png")
        #blank.save(response, "PNG")
        #return response
        filename_action = './images/action_default.jpg'
        with open(filename_action, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")

    raise Http404() # Ættum ekki að koma hingað

@cache_page(60 * 60 * 24 * 7)
def club_logo(request, ClubName):
    ClubName_decode = urllib.parse.unquote(ClubName).lower()
    try: # Reyna png
        filename = './images/clubs/{}.png'.format(ClubName_decode)
        with open(filename, "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except:
        try: # Reyna svg
            filename = './images/clubs/{}.svg'.format(ClubName_decode)
            with open(filename, "rb") as f:
                return HttpResponse(f.read(), content_type="image/svg+xml")
        except:
            try: # Reyna jpg
                filename = './images/clubs/{}.jpg'.format(ClubName_decode)
                with open(filename, "rb") as f:
                    return HttpResponse(f.read(), content_type="image/jpeg")
            except: # Ekkert virkar skila þá 404
                raise Http404()

@cache_page(60 * 60 * 24)
def competitor_records(request, CompetitorCode):
    Records = records.Get_Competitor_Records(CompetitorCode)
    return JsonResponse(Records, safe=False)

@cache_page(60 * 60 * 6)
def record_birthdays(request):
    Records = records.Get_Records_Birthdays()
    return JsonResponse(Records, safe=False)

@cache_page(60 * 60 * 0)
def national_records_all(request):
    df = records.Get_All_National_Records()
    return df

#@cache_page(60 * 60 * 24)
#def national_records_masters(request):
#    df = records.Get_All_Master_Records()
#    return df

@cache_page(60 * 60 * 0)
def national_records(request):
    #df_records = national_records_all(request)
    df_records = records.Get_All_National_Records()
    #df_masters = national_records_masters(request)
    #df_masters = records.Get_All_Master_Records()

    List_of_Records = []

    # Adults and 12-22 year old
    for index, row in df_records.iterrows():
        if (row['Nafn'] != None): # Aðgerðin í gagnagrunninum virðist skila út NULL á milli aldursflokka
            try:
                Event_Info = events.Get_Event_Info_by_Name(row['HeitiGreinar'])
            except:
                print(row)
            List_of_Records.append({
                'Event': Event_Info['NAME_SHORT'],
                'Results': row['Arangur'],
                'Wind': row['Vindur'],
                'Name': row['Nafn'],
                'Club': row['Félag'],
                'Place': row['Staður'],
                'Date': format_date(row['Dagsetn'].date(), "d MMM yyyy", locale='is_IS').upper(),
                'CompetitorID': row['Keppandan'],
                'AgeGroup': row['AldursflFRÍ'],
                'Sex': row['Ky'],
                'InOut': row['ÚtiInni'],
                'Units_symbol': Event_Info['UNIT_SYMBOL']
            })

    return JsonResponse(List_of_Records, safe=False)

@cache_page(60 * 60 * 24)
def national_records_masters(request):
    #df_records = national_records_all(request)
    #df_records = records.Get_All_National_Records()
    #df_masters = national_records_masters(request)
    df_masters = records.Get_All_Master_Records()

    List_of_Records = []
    
    # Masters records
    for index, row in df_masters.iterrows():
        if (row['Nafn'] != None):
            Event_Info = events.Get_Event_Info_by_Name(row['HeitiGr'])
            List_of_Records.append({
                'Event': Event_Info['NAME_SHORT'],
                'Results': row['Árang'],
                'Wind': row['Vindur'],
                'Name': row['Nafn'],
                'Club': row['Félag'],
                'Place': row['Staður'],
                'Date': format_date(row['Dags'].date(), "d MMM yyyy", locale='is_IS').upper(),
                'CompetitorID': row['Keppandan'],
                'AgeGroup': row['Aldursflokkuröldunga'],
                'Sex': row['Ky'],
                'InOut': int(row['ÚtiInni']),
                'Units_symbol': Event_Info['UNIT_SYMBOL']
            })

    return JsonResponse(List_of_Records, safe=False)
