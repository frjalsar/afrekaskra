from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek
from django.db.models import Q

# Settings
from Sif import settings

# Other packages
import datetime
import pytz
import pandas as pd
import numpy as np
import os
from babel.dates import format_date, format_datetime, format_time

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

# Units
Units_symbol = {1: 'm', 2: 's', 3: 'mm:ss,dd', 4: 'hh:mm:ss,dd', 5: 'stig', 6: 'stig'}

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
        print(in_str)
        raise ValueError()
        return None

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

        Event_Info = {'THORID_1': df_event_list['THORID_1'].values[Event_id],
                      'Units': Units,
                      'Units_symbol': Units_symbol[Units],
                      'Minimize': minimize,
                      'ShortName': df_event_list['ShortName'].values[Event_id],
                      'Name_ISL': df_event_list['Name_ISL'].values[Event_id],
                      'HasWind': df_event_list['Wind'].values[Event_id]}
    except:
        raise Http404('Gat ekki fundið grein.')

    return Event_Info

def Convert_Achievements_to_List_PD(q, best_by_ath, Event_Info):
    df = pd.DataFrame.from_records(q.values_list('lína', 'nafn', 'keppandanúmer',
                                                 'árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni'),
                                                 columns=['lína', 'nafn', 'keppandanúmer',
                                                          'árangur', 'vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni'])

    df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['árangur_float'] = df['árangur'].map(results_to_float)

    # Röðum árangri, fyrst eftir árangri og svo eftir dagsetningu ef árangrar eru jafnir.
    if (Event_Info['Minimize'] == True):
        df.sort_values(by=['árangur_float', 'dagsetning'], ascending=[True, True], inplace=True)
    else:
        df.sort_values(by=['árangur_float', 'dagsetning'], ascending=[False, True], inplace=True)

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

        if (row.rafmagnstímataka == 0 and Event_Info['Minimize'] == True):
            result_str = '{:.1f}'.format(row.árangur_float)
        else:
            if (Event_Info['Units'] == 5):
                result_str = '{:.0f}'.format(row.árangur_float)
            else:
                result_str = '{:.2f}'.format(row.árangur_float)

        Achievement_info = {'name': row.nafn,
                            'results': result_str,
                            'wind': wind_str,
                            'club': row.félag,
                            'age': row.aldur_keppanda,
                            'competition_name': row.heiti_móts,
                            'competition_id': row.mót,
                            'outdoor_indoor': row.úti_inni, 
                            'date': date_str,
                            'competitor_code': row.keppandanúmer,
                            'electronic_timing': row.rafmagnstímataka
                            }
        Achievements_list.append(Achievement_info)

    #print(df.head(n=10))
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
        #event_list = Get_List_of_Events(CompetitorCode=CompetitorCode, Event_id=None)
        
        # Make a Competitor dict with information about the competitor
        Competitor_Info = {'CompetitorCode': CompetitorCode,
                           'Name': q.nafn,
                           'FirstName': q.nafn.split(' ')[0],
                           'LastName': q.nafn.split(' ')[-1],
                           'YOB': q.fæðingarár,
                           'Club': q.félag
                           #'Datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                           #'Events': event_list
                           }
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info

def Get_Competitor_Events_Info(CompetitorCode=None):
    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode)
    df = pd.DataFrame.from_records(q.values_list('lína', 'nafn', 'keppandanúmer',
                                                 'árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                 'grein', 'tákn_greinar', 'vantar_vind'),
                                                 columns=['lína', 'nafn', 'keppandanúmer',
                                                          'Árangur', 'Vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                          'grein', 'tákn_greinar', 'vantar_vind'])

    # úti_inni: Úti = 0, Inni = 1
    df['Dagsetn.'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['Árangur_float'] = df['Árangur'].map(results_to_float)

    # Búa til lista yfir greinar
    list_events = df['tákn_greinar'].copy() # copy til að búa til afrit
    list_events.drop_duplicates(inplace=True) # Henda út endurtekningum
    list_events.reset_index(drop=True, inplace=True) # Endur númera index

    list_pb = []
    list_sb = []
    for i in list_events:
        event_id = df_event_list[df_event_list['THORID_1'] == i].index.tolist()[0]
        event_info = Get_Event_Info(event_id)
        #print(event_info)

        # Flokka út Grein
        df_event = df.loc[df['tákn_greinar'] == i].copy() # Búum til copy til að breyta
        df_event.reset_index(drop=True, inplace=True) # Endur númera index

        # Úti árangur með löglegum vindi
        mask = np.logical_and(df_event['Vindur'] <= 2.0, df_event['úti_inni'] == 0)
        #mask = np.logical_and(mask, df_event['vantar_vind'] == 0)
        df_event_nowind_out = df_event.loc[mask]

        df_event_out = df_event.loc[df_event['úti_inni'] == 0] # Úti árangur + vind árangur
        df_event_in = df_event.loc[df_event['úti_inni'] == 1] # Inni árangur

        #print(df_event_out.head(n=10))

        # Telja hve oft viðkomandi hefur keppt í þessari grein
        count = df_event['Árangur'].count()

        pb_out = ''
        pb_in = ''

        #try:
            # Finnum PB inni ef það er til
        if (df_event_in.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_in['Árangur_float'].idxmax()
            else:
                idx = df_event_in['Árangur_float'].idxmin()

            pb_in = df_event_in['Árangur'][idx]

        # Finnum PB úti með löglegum árangri ef það er til
        if (df_event_nowind_out.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_nowind_out['Árangur_float'].idxmax()
            else:
                idx = df_event_nowind_out['Árangur_float'].idxmin()

            pb_out = df_event_nowind_out['Árangur'][idx]

        # Ef ekki þá athugum við ólöglegan árangur
        elif (df_event_out.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_out['Árangur_float'].idxmax()
            else:
                idx = df_event_out['Árangur_float'].idxmin()

            pb_out = df_event_out['Árangur'][idx] + ' ({:+.1f}'.format(df_event_out['Vindur'][idx]) + ' m/s)'
        #except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
        #    pass


        # Fyrir SB
        # date_now = datetime.date.today()
        # if (date_now.month >= 11):
        #     date_to_in = date_now
        #     date_from_in = datetime.datetime(date_now.year, 11, 1, 0, 0, 0) # 1 Nov
        #
        #     date_to_out = datetime.datetime(date_now.year, 10, 31, 0, 0, 0) # 31 Okt
        #     date_from_out = datetime.datetime(date_now.year, 5, 1, 0, 0, 0) # 1 Maí
        # elif (date_now.month <= 4):
        #     date_to_in = date_now
        #     date_from_in = datetime.datetime(date_now.year-1, 11, 1, 0, 0, 0) # 1 Nov í fyrra
        #
        #     date_to_out = datetime.datetime(date_now.year-1, 10, 31, 0, 0, 0) # 30 Okt í fyrra
        #     date_from_out = datetime.datetime(date_now.year-1, 5, 1, 0, 0, 0) # 1 Maí í fyrra
        # else:
        #     date_to_in = datetime.datetime(date_now.year, 4, 30, 0, 0, 0) # 30 Apr
        #     date_from_in = datetime.datetime(date_now.year-1, 11, 1, 0, 0, 0) # 1 Nov
        #
        #     date_to_out = date_now
        #     date_from_out = datetime.datetime(date_now.year, 5, 1, 0, 0, 0) # 1 Maí


        # date_now = pd.Timestamp( datetime.date.today() )
        # date_later = pd.Timestamp( datetime.date.today() + datetime.timedelta(days=-240) ) # 8*30 = 240, 8 mánuðir, ath mínus
        # date_to_out = date_now
        # date_from_out = date_later
        # date_to_in = date_now
        # date_from_in = date_later

        # mask_out = np.logical_and(df_event_out['Dagsetn.'] < date_to_out, date_from_out < df_event_out['Dagsetn.'])
        # mask_nowind_out = np.logical_and(df_event_nowind_out['Dagsetn.'] < date_to_out, date_from_out < df_event_nowind_out['Dagsetn.'])
        # mask_in = np.logical_and(df_event_in['Dagsetn.'] < date_to_in, date_from_in < df_event_in['Dagsetn.'])

        # df_event_sb_out = df_event_out.loc[mask_out]
        # df_event_nowind_sb_out = df_event_nowind_out.loc[mask_nowind_out]
        # df_event_sb_in = df_event_in.loc[mask_in]

        sb_out = ''
        sb_in = ''

        # try:
        #     # Finnum SB inni ef það er til
        #     if (df_event_sb_in.empty == False):
        #         if (event_max == True):
        #             idx = df_event_sb_in['Árangur_float'].idxmax()
        #         else:
        #             idx = df_event_sb_in['Árangur_float'].idxmin()

        #         sb_in = df_event_sb_in['Árangur'][idx]

        #     # Finnum SB úti með löglegum árangri ef það er til
        #     if (df_event_nowind_sb_out.empty == False):
        #         if (event_max == True):
        #             idx = df_event_nowind_sb_out['Árangur_float'].idxmax()
        #         else:
        #             idx = df_event_nowind_sb_out['Árangur_float'].idxmin()

        #         sb_out = df_event_nowind_sb_out['Árangur'][idx]

        #     # Ef ekki þá athugum við ólöglegan árangur
        #     elif (df_event_sb_out.empty == False):
        #         if (event_max == True):
        #             idx = df_event_sb_out['Árangur_float'].idxmax()
        #         else:
        #             idx = df_event_sb_out['Árangur_float'].idxmin()

        #         sb_out = df_event_osb_ut['Árangur'][idx] + ' (' + Wind_as_str(df_event_sb_out['Vindur'][idx]) + ' m/s)'
        # except:
        #     # Ef eitthvað klikkar þá sleppum við þessari grein
        #     pass

        # Bæta við í listan
        list_pb.append({'Event': event_info['Name_ISL'] + ' [' + event_info['Units_symbol'] + ']', 'PB_out': pb_out, 'PB_in': pb_in, 'SB_out': sb_out, 'SB_in': sb_in, 'count': int(count)})

    # Röðum listanum í öfuga röð eftir því oft hefur verið keppt í greinunum
    # Þarf ekki því html taflan gerir þetta líka!!
    list_pb.sort(key=lambda dic: dic['count'], reverse=True)

    #print(list_pb)

    return list_pb

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

# Get_Competitor_Info
# Looks upp information about a competitor from the AthlCompetitors table.
# Inn:
#  CompetitorCode: Fiffós ID code for the competitor
# Out:
#  Competitor_Info: A dictionary containing name, year of birth and club.
def Get_Competitor_Data(CompetitorCode):
    Test_List_of_Events(CompetitorCode=CompetitorCode, Event_id = None)
    return None

def Top_100_List(Event_id, Year, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal, ISL, BestByAth):
    if (Event_id > 1000): # Ef Event_id ef yfir 1000 þá er þetta þrautagrein. Þurfum að meðhöndla þær sérstaklega.
        Athlon_events = {1001: 'FIMMTARÞR',  # Fimmtarþraut
                         1002: 'FIMMTUNG',   # Fimmtarþr. unglingastig
                         1003: 'FIMMTAR76C', # Fimmtarþraut (76cm grind)
                         1004: 'FIMMTARÞ15', # Fimmtarþraut pilta 15 ára

                         1011: 'SJÖÞRAUT',   # Sjöþraut
                         1012: 'SJÖÞRAUT6K', # Sjöþraut (6Kg kúla) 
                         1013: 'SJÖÞRAUT5K', # Sjöþraut (5Kg kúla)
                         1014: 'SJÖÞRAUT',   # Sjöþraut meyjaáhöld

                         1021: 'TUGÞRAUT',   # Tugþraut
                         1022: 'TUGÞRAU17',  # Tugþraut 16-17 ára
                         1023: 'TUGÞRRU20'}  # Tugþraut U20 (Norðurlönd)

        THORID_2 = Athlon_events[Event_id]

        Event_Info = {'THORID_1': '',
                      'Units': 5,
                      'Units_symbol': 'Stig',
                      'Minimize': False,
                      'ShortName': '',
                      'HasWind': 0}
        q = AthlAfrek.objects.all().filter(grein__iexact=THORID_2)
        if ((Event_id == 1002) or (Event_id == 1014)):
            q = q.filter(flokkur=14)

    else:
        Event_Info = Get_Event_Info(Event_id)
        q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=Event_Info['THORID_1'])

    #--
    if (Event_Info['Minimize'] == True):
        #order_by_str = 'árangur'
        if (Legal == 1):
            electime = 1
            # Gagnagrunurinn er með dálk sem heitir löglegt. En það virðist ekki vera hægt að treysta honum.
            # Ólögleigir árangrar eru flokkaðir sem vindur > 2.0, vantar vind og/eða handtímataka
            q = q.filter(vindur__lte=2.00, rafmagnstímataka=electime, vantar_vind=0)
    else: # Dálkurinn með rafmagnstímataka getur verið hvað sem er í greinum sem eru ekki með tímatöku.
        if (Legal == 1):
            q = q.filter(vindur__lte=2.00, vantar_vind=0)
    #    order_by_str = '-árangur'

    q = q.filter(kyn=Gender, aldur_keppanda__range=[AgeStart, AgeEnd])

    if (IndoorOutDoor != 2): # 2 þýðir bæði úti og inni árangur
        q = q.filter(úti_inni=IndoorOutDoor)

    # Ef við viljum fá öll gögn þá er Year = 0
    if (Year > 0):
        q = q.filter(dagsetning__gte=datetime.datetime(Year, 1, 1, tzinfo=pytz.UTC),
                     dagsetning__lte=datetime.datetime(Year, 12, 31, tzinfo=pytz.UTC))

    # Öll þjóðerni eða ekki. ISL = 0 þýðir bara íslendingar.
    if (ISL == 0):
        q = q.filter(erlendur_ríkisborgari=0)

    # q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=THORID_1,
    #                                    úti_inni=IndoorOutDoor,
    #                                    kyn=Gender,
    #                                    dagsetning__gte=datetime.date(Year, 1, 1),
    #                                    dagsetning__lte=datetime.date(Year, 12, 31)).order_by(order_by_str)[:1000]

    #q = q.order_by(order_by_str)
    #Achievements_list = Convert_Achievements_to_List(q, minimize_results, BestByAth, Units)
    Achievements_list = Convert_Achievements_to_List_PD(q, BestByAth, Event_Info)

    return Achievements_list[:100], Event_Info

def Get_Competitor_List(q):

    names_q = AthlAfrek.objects.all()

    for i in q.split():
            names_q = names_q.filter(
              Q(nafn__icontains=i)
            | Q(félag__icontains=i)
            | Q(fæðingarár__icontains=i) )

            # Taka saman niðurstöðunar
    results = []

    df = pd.DataFrame.from_records(names_q.values_list('keppandanúmer', 'nafn', 'fæðingarár', 'félag'),
                                              columns=['keppandanúmer', 'nafn', 'fæðingarár', 'félag'])

    df.drop_duplicates(subset=['keppandanúmer'], keep='first', inplace=True, ignore_index=True)

    # Hendum út öllu sem er ekki í top 100
    df = df.iloc[0:100]

    for index, row in df.iterrows():
        Competitor_Info = {'CompetitorCode': row.keppandanúmer,
                           'Name': row.nafn,
                           'FirstName': row.nafn.split(' ')[0],
                           'LastName': row.nafn.split(' ')[-1],
                           'YOB': row.fæðingarár,
                           'Club': row.félag
                           }
        results.append(Competitor_Info)

    #sb_json = { 'results': results,
    #            'pagination': [ {'more': False} ] }
    return results