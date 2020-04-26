from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek

# Settings
from Sif import settings

# Other packages
import datetime
import pandas as pd
import os
from babel.dates import format_date, format_datetime, format_time

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

def Get_Event_ThorID_1(Event_id):
    try:
        THORID_1 = df_event_list['THORID_1'].values[Event_id]
    except:
        raise Http404('Gat ekki fundið grein.')
    return THORID_1

def Convert_Achievements_to_List(q):
    Achievements_list = []
    for Achievement in q:
        # Make wind into a string with sign. One decimal after period.
        wind_str = '{:+.1f}'.format(float(Achievement.vindur))

        # Turn results into string with two decimals after period or one if hand timing.
        if (Achievement.rafmagnstímataka == 0):
            result_str = '{:.1f}'.format(float(Achievement.árangur.replace(',', '.')))
        else:
            result_str = '{:.2f}'.format(float(Achievement.árangur.replace(',', '.')))

        # Turn the date into a string
        date_str = format_date(Achievement.dagsetning.date(), "d MMM yyyy",locale='is_IS').upper()

        # Data
        Achievement_info = {'name': Achievement.nafn,
                            'results': result_str,
                            'wind': wind_str,
                            'club': Achievement.félag,
                            'age': Achievement.aldur_keppanda,
                            'outdoor_indoor': Achievement.úti_inni,
                            'legal': Achievement.löglegt,
                            'competition_name': Achievement.heiti_móts,
                            'competition_id': Achievement.mót,
                            'date': date_str,
                            'location': Achievement.staður,
                            'competitorcode': Achievement.keppandanúmer
                            }

        # Append
        Achievements_list.append(Achievement_info)

    return Achievements_list


# Get_List_of_Achievements
# Looks upp all achievements for a competitor in an given event from the AthlCompetitors table.
# Inn:
#  CompetitorCode: Fiffós ID code for the competitor
#  Event_id: The number of the event. This is our new ID not Fiffós.
# Out:
#   A list of dictionaries containing information about each achievement.
def Get_List_of_Achievements(CompetitorCode, Event_id):
    THORID_1 = Get_Event_ThorID_1(Event_id)

    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode).filter(tákn_greinar__iexact=THORID_1)
    Achievements_list = Convert_Achievements_to_List(q)

    return Achievements_list

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

def Top_100_List(Event_id, Year, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal):
    THORID_1 = Get_Event_ThorID_1(Event_id)

    if (Year == 0):
        q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=THORID_1,
                                           aldur_keppanda__range=[AgeStart, AgeEnd],
                                           löglegt=Legal,
                                           úti_inni=IndoorOutDoor,
                                           kyn=Gender).order_by('árangur')[:100]
    else:
        q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=THORID_1,
                                           aldur_keppanda__range=[AgeStart, AgeEnd],
                                           dagsetning__gte=datetime.date(Year, 1, 1),
                                           dagsetning__lte=datetime.date(Year, 12, 31),
                                           löglegt=Legal,
                                           úti_inni=IndoorOutDoor,
                                           kyn=Gender).order_by('árangur')[:100]

    Achievements_list = Convert_Achievements_to_List(q)

    return Achievements_list