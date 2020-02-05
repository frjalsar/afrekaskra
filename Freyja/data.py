from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Freyja.models import AthlCompetitors, AthlAfrek

# Settings
from Freyja import settings

# Other packages
import datetime
import pandas as pd
import os

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Freyja/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

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
        event_list = Get_List_of_Events(CompetitorCode=CompetitorCode, Event_id=None)
        
        # Make a Competitor dict with information about the competitor
        Competitor_Info = {'CompetitorCode': CompetitorCode,
                           'Name': q.nafn,
                           'FirstName': q.nafn.split(' ')[0],
                           'LastName': q.nafn.split(' ')[-1],
                           'YOB': q.fæðingarár,
                           'Club': q.félag,
                           #'Datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                           'Events': event_list}
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info

def Get_List_of_Events(CompetitorCode=None, Event_id=None):
    if (CompetitorCode == None):
        q = AthlAfrek.objects.order_by('tákn_greinar').values_list('tákn_greinar', flat=True).distinct()
    else:
        q = AthlAfrek.objects.values_list('tákn_greinar', flat=True).distinct().filter(keppandanúmer__iexact=CompetitorCode)

    Event_list = []
    for event in q:
        try:
            event_info = {'EVENT_ID': int(df_event_list[df_event_list['THORID_1'] == event].index[0]),
                        'Name_ISL': df_event_list[df_event_list['THORID_1'] == event]['Name_ISL'].values[0],
                        'Name_ENG': df_event_list[df_event_list['THORID_1'] == event]['Name_ENG'].values[0],
                        'Name_short': df_event_list[df_event_list['THORID_1'] == event]['ShortName'].values[0],
                        'Units': int(df_event_list[df_event_list['THORID_1'] == event]['Units'].values[0]),
                        'Wind': bool(df_event_list[df_event_list['THORID_1'] == event]['Wind'].values[0])}
            if (Event_id == None):
                Event_list.append(event_info)
            elif (Event_id == event_info['EVENT_ID']):
                Event_list.append(event_info)
        except:
            print('Error event not found')
            print(event)
            pass

    return Event_list