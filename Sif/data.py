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

# Units
Units_symbol = {1: 'm', 2: 's', 3: 'mm:ss', 4: 'hh:mm:ss,dd', 5: 'stig', 6: 'stig'}

# stuff
import re
prog_time = re.compile('^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?(\d+\.?\d*)?$') # Notum regex

#-------------------------------------------------------------------------------
# Fall sem breytir streng með árangri yfir í rauntölu
# '65.76' -> 65.76
# ''      -> NaN
# 'ABCD'  -> NaN
# Ef strengurinn er tími á forminu HH:MM:SS.FF þá er honum breytt yfir í sek
# '02:43.45' -> 2*60 + 43.45 = 163.45
# '01:02.45' -> 1*60*60 + 2*60 + 43.45 = 3763.45
def results_to_float(in_str):
    #prog_time = re.compile('^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?(\d+\.?\d*)?$') # Notum regex
    m = prog_time.match(str(in_str).replace(',', '.'))
    if (m): # Athuga hvort við fengum match

        if (m.group(1) is None and m.group(2) is None and m.group(3) is None):
            return np.nan # Eitthvað skrítið í gagni eða tómur strengur skila NaN

        time_sec = 0.0 # Breytum yfir í sek ef þetta er tími
        if (m.group(1) is not None):
            time_sec = float(m.group(1))*3600.0 # 60*60 = 3600
        if (m.group(2) is not None):
            time_sec = time_sec + float(m.group(2))*60.0
        if (m.group(3) is not None):
            time_sec = time_sec + float(m.group(3))

        return time_sec
    else:
        return np.nan # Fengum ekki match skilum NaN

def Get_List_of_Years():
    #df = pd.DataFrame(list(AthlAfrek.objects.values('dagsetning')))
    #df['year'] = pd.DatetimeIndex(df['dagsetning']).year
    #df = df.sort_values(by=['year'], ascending=False)
    #return list(df.year.unique())

    # It takes a long time to get the list of all dates from the database because the Django drivers for MS-SQL doesn't support distinct.
    current_year = datetime.datetime.now().year
    return list(range(current_year, 1909-1, -1))

def Get_Event_Info(Event_id):
    try:
        THORID_1 = df_event_list['THORID_1'].values[Event_id]
        Units = df_event_list['Units'].values[Event_id]
        #0, # No units!
        #'metrar': 1, # Meters
         #'sek.': 2, # ss,dd
         #'mín.': 3, # mm:ss
         #'klst.': 4, # hh:mm:ss,dd
         #'stig': 5, # Points
         #'Ungl.stig': 6 # Points junior
        if (Units in [0, 2, 3, 4]):
            minimize = True
        else:
            minimize = False
    except:
        raise Http404('Gat ekki fundið grein.')

    return THORID_1, Units, minimize

def Convert_Achievements_to_List_PD(q, minimize_results, best_by_ath, units):
    df = pd.DataFrame.from_records(q.values_list('lína', 'nafn', 'keppandanúmer',
                                                 'árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka'),
                                                 columns=['lína', 'nafn', 'keppandanúmer',
                                                          'árangur', 'vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka'])

    df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['árangur_float'] = df['árangur'].map(results_to_float)

    # Röðum árangri, fyrst eftir árangri og svo eftir dagsetningu ef árangrar eru jafnir.
    if (minimize_results == True):
        df.sort_values(by=['árangur_float', 'dagsetning'], ascending=[True, False], inplace=True)
    else:
        df.sort_values(by=['árangur_float', 'dagsetning'], ascending=[False, False], inplace=True)

    # Athuga hvort við viljum bara besta árangur íþróttamanns. Ef svo er hendum við úr endurtekningum en höldum fyrstu línu.
    if (best_by_ath == True):
        df.drop_duplicates(subset=['keppandanúmer'], keep='first', inplace=True, ignore_index=True)

    # Hendum út öllu sem er ekki í top 100
    df = df.iloc[0:100]

    # Skipta út NaN fyrir 0.0 í vind (Innanhús árangur og árangur þar sem ekki er mældur vindur)
    df['vindur'].fillna(0.0, inplace=True)

    Achievements_list = []
    for index, row in df.iterrows():
        date_str = format_date(row.dagsetning.date(), "d MMM yyyy",locale='is_IS').upper()
        wind_str = '{:+.1f}'.format(row.vindur)

        if (row.rafmagnstímataka == 0 and minimize_results == True):
            result_str = '{:.1f}'.format(row.árangur_float)
        else:
            result_str = '{:.2f}'.format(row.árangur_float)

        Achievement_info = {'name': row.nafn,
                            'results': result_str,
                            'wind': wind_str,
                            'club': row.félag,
                            'age': row.aldur_keppanda,
                            'competition_name': row.heiti_móts,
                            'competition_id': row.mót,
                            'date': date_str,
                            'competitorcode': row.keppandanúmer
                            }
        Achievements_list.append(Achievement_info)

    print(df.head(n=10))
    return Achievements_list

def Convert_Achievements_to_List(q, minimize_results, best_by_ath, units):
    Achievements_list = []
    competitorcode_list = []

    for Achievement in q:
        # Make wind into a string with sign. One decimal after period.
        wind_str = '{:+.1f}'.format(float(Achievement.vindur))

        # Turn results into string with two decimals after period or one if hand timing.
        results = results_to_float(Achievement.árangur.replace(',', '.'))
        try:
            if (Achievement.rafmagnstímataka == 0 and minimize_results == True):
                result_str = '{:.1f}'.format(results)
            else:
                result_str = '{:.2f}'.format(results)
        except:
            print('Error')
            print(Achievement.lína)
            print(Achievement.nafn)
            print(Achievement.árangur)
            print(Achievement.keppandanúmer)
            print('')
            result_str = 'ERROR'

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
        if (best_by_ath == 1):
            if (Achievement_info['competitorcode'] in competitorcode_list):
                continue
        
        competitorcode_list.append(Achievement_info['competitorcode'])
        Achievements_list.append(Achievement_info)

    if not q:
        Achievement_info = {'name': 'Enginn gögn fundust :(',
                            'results': '',
                            'wind': '',
                            'club': '',
                            'age': '',
                            'outdoor_indoor': '',
                            'legal': '',
                            'competition_name': '',
                            'competition_id': '',
                            'date': '',
                            'location': '',
                            'competitorcode': ''
                            }
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
    THORID_1, _, _ = Get_Event_Info(Event_id)

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

def Top_100_List(Event_id, Year, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal, ISL, BestByAth):
    THORID_1, Units, minimize_results = Get_Event_Info(Event_id)
    q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=THORID_1,
                                       úti_inni=IndoorOutDoor,
                                       kyn=Gender,
                                       aldur_keppanda__range=[AgeStart, AgeEnd])

    if (minimize_results == True):
        order_by_str = 'árangur'
        if (Legal == 1):
            electime = 1
            # The database has a field named löglegt, but it cannot be trusted. So we filter out wind less than 2.0
            q = q.filter(vindur__lte=2.00, rafmagnstímataka=electime)
    else:
        if (Legal == 1):
             q = q.filter(vindur__lte=2.00)
        order_by_str = '-árangur'

    if (Year > 0):
        q = q.filter(dagsetning__gte=datetime.date(Year, 1, 1),
                     dagsetning__lte=datetime.date(Year, 12, 31))

    if (ISL == 0):
        q = q.filter(erlendur_ríkisborgari=0)

    # q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=THORID_1,
    #                                    úti_inni=IndoorOutDoor,
    #                                    kyn=Gender,
    #                                    dagsetning__gte=datetime.date(Year, 1, 1),
    #                                    dagsetning__lte=datetime.date(Year, 12, 31)).order_by(order_by_str)[:1000]

    q = q.order_by(order_by_str)
    #Achievements_list = Convert_Achievements_to_List(q, minimize_results, BestByAth, Units)
    Achievements_list = Convert_Achievements_to_List_PD(q, minimize_results, BestByAth, Units)

    return Achievements_list[:100]