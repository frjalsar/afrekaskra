from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors
from django.db.models import Q
from django.db import connection

# Settings
from Sif import settings

# Other packages
import datetime
import pytz
import pandas as pd
import numpy as np
import os
from babel.dates import format_date, format_datetime, format_time

from Sif import common
from Sif import events
from Sif import competitor


CLUB_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/clubs.csv')


def Get_List_of_Years():
    #df = pd.DataFrame(list(AthlAfrek.objects.values('dagsetning')))
    #df['year'] = pd.DatetimeIndex(df['dagsetning']).year
    #df = df.sort_values(by=['year'], ascending=False)
    #return list(df.year.unique())

    # It takes a long time to get the list of all dates from the database because the Django drivers for MS-SQL doesn't support distinct.
    current_year = datetime.datetime.now().year
    return list(range(current_year, 1909-1, -1))

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
    df['árangur_float'] = df['árangur'].map(common.results_to_float)

    # Bæta við buffer ef tíminn er handtími
    hand_buffer = common.Get_Hand_buffer(Event_Info['Distance'])

    # Búum til nýjan dálk þar sem búið er að bæta við buffer tímanum.
    # Flokkum svo eftir þeim dálk.
    df['árangur_sort'] = df['árangur_float'].copy()
    for index, row in df.iterrows():
        if row['rafmagnstímataka'] == 1:
            df.loc[index, 'árangur_sort'] = row['árangur_float']
        else:
            df.loc[index, 'árangur_sort'] = row['árangur_float'] + hand_buffer

    # Röðum árangri, fyrst eftir árangri og svo eftir dagsetningu ef árangrar eru jafnir.
    if (Event_Info['Minimize'] == True):
        df.sort_values(by=['árangur_sort', 'dagsetning'], ascending=[True, True], inplace=True)
    else:
        df.sort_values(by=['árangur_sort', 'dagsetning'], ascending=[False, True], inplace=True)

    # Athuga hvort við viljum bara besta árangur íþróttamanns. Ef svo er hendum við úr endurtekningum en höldum fyrstu línu.
    if (best_by_ath == True):
        df.drop_duplicates(subset=['keppandanúmer'], keep='first', inplace=True, ignore_index=True)

    # Hendum út öllu sem er ekki í top 100
    df = df.iloc[0:100]

    # Skipta út NaN fyrir 0.0 í vind (Innanhúss árangur og árangur þar sem ekki er mældur vindur)
    df['vindur'].fillna(0.0, inplace=True)

    Achievements_list = []
    for index, row in df.iterrows():
        date_str = format_date(row.dagsetning.date(), "d MMM yyyy",locale='is_IS').upper()
        wind_str = '{:+.1f}'.format(row.vindur)

        # if (row.rafmagnstímataka == 0 and Event_Info['Minimize'] == True):
        #     result_str = '{:.1f}'.format(row.árangur_float)
        # else:
        #     if (Event_Info['Units'] == 5):
        #         result_str = '{:.0f}'.format(row.árangur_float)
        #     else:
        #         result_str = '{:.2f}'.format(row.árangur_float)

        if (row.rafmagnstímataka == 1):
            ElecTime = True
        else:
            ElecTime = False
        result_str = common.results_to_str(row.árangur_float, Event_Info['Units'], ElecTime, Event_Info['Distance'])

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
        results = common.results_to_float(Achievement.árangur.replace(',', '.'))
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
        date_str = format_date(Achievement.dagsetning.date(), "d MMM yyyy", locale='is_IS').upper()

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
    THORID_1, _, _ = events.Get_Event_Info_by_ID(Event_id)

    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode).filter(tákn_greinar__iexact=THORID_1)
    Achievements_list = Convert_Achievements_to_List(q)

    return Achievements_list

def Top_100_List(Event_id, fromDate, toDate, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal, ISL, BestByAth, N=100):
    # Sumar greinar eru skráðar oftar ein einu sinni í Þór. Í því tilviki notum við bara ThorID 1 til að fletta þeim upp.
    Event_id_double_thorid_1 = [228, 232, 233, # Spjótkast 500 gr
                                229, 231, # Spjótkast 700 gr
                                155, 156, # Kringlukast 600 gr
                                183, 187] # Lóðkast 11,34 kg

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

        Athlon_events_Name = {1001: 'Fimmtarþraut',  # Fimmtarþraut
                         1002: 'Fimmtarþr. unglingastig',   # Fimmtarþr. unglingastig
                         1003: 'Fimmtarþraut (76cm grind)', # Fimmtarþraut (76cm grind)
                         1004: 'Fimmtarþraut pilta 15 ára', # Fimmtarþraut pilta 15 ára

                         1011: 'Sjöþraut',   # Sjöþraut
                         1012: 'Sjöþraut (6Kg kúla)', # Sjöþraut (6Kg kúla)
                         1013: 'Sjöþraut (5Kg kúla)', # Sjöþraut (5Kg kúla)
                         1014: 'Sjöþraut meyjaáhöld',   # Sjöþraut meyjaáhöld

                         1021: 'Tugþraut',   # Tugþraut
                         1022: 'Tugþraut 16-17 ára',  # Tugþraut 16-17 ára
                         1023: 'Tugþraut U20 (Norðurlönd)'}  # Tugþraut U20 (Norðurlönd)

        THORID_2 = Athlon_events[Event_id]

        Event_Info = {'THORID_1': '',
                      'Units': 5,
                      'Units_symbol': 'Stig',
                      'Minimize': False,
                      'ShortName': Athlon_events_Name[Event_id],
                      'HasWind': 0,
                      'Distance': -1.0}
        q = AthlAfrek.objects.all().filter(grein__iexact=THORID_2)
        if ((Event_id == 1002) or (Event_id == 1014)):
            q = q.filter(flokkur=14)

    else:
        Event_Info = events.Get_Event_Info_by_ID(Event_id)
        #Event_Info = event.Get_Event_Info_by_ID_New(Event_id)
        flokkur = Event_Info['AgeGroup']
        if (flokkur == '-1'):
            flokkur = ''

        if (Event_id in Event_id_double_thorid_1):
            q = AthlAfrek.objects.all().filter(tákn_greinar__iexact=Event_Info['THORID_1'])
        else:
            # Athuga greinar sem eru skráðar oftar en einu sinni
            match Event_id:
                case 165:# Kúluvarp 6kg
                    # Kúluvarp 6 kg er þrískráð sem grein
                    # THORID_2 = KÚLA   , THORID_1 = KÚLA6K
                   # THORID_2 = KÚLA6KG, THORID_1 = KÚLA6KG6K
                    # THORID_2 = KÚLA6KG, THORID_1 = KÚLA6KG5K
                    q = AthlAfrek.objects.all().filter(Q(grein__iexact="KÚLA", tákn_greinar__iexact="KÚLA6K") |
                                                   Q(grein__iexact="KÚLA6KG", tákn_greinar__iexact="KÚLA6KG6K") |
                                                   Q(grein__iexact="KÚLA6KG", tákn_greinar__iexact="KÚLA6KG5K"))
                case 172: # Kúluvarp 5 KG
                    # Kúluvarp 5 KG er tvískráð
                    # THORID_2 = KÚLA    , THORID_1 = KÚLA5K
                    # THORID_2 = KÚLA5KG, THORID_1 = KÚLA5KG5K
                    q = AthlAfrek.objects.all().filter(Q(grein__iexact="KÚLA", tákn_greinar__iexact="KÚLA5K") |
                                                       Q(grein__iexact="KÚLA5KG", tákn_greinar__iexact="KÚLA5KG5K"))
                case 188: # Lóðkast 15,88 kg
                    # Tvískráð
                    q = AthlAfrek.objects.all().filter(Q(tákn_greinar__iexact="LÓÐ11,34K"))
                case 183: # Lóðkast 11,34 kg
                    # Tvískráð
                    q = AthlAfrek.objects.all().filter(Q(grein__iexact="LÓÐ1588"))
                case 182: # Lóðkast 9,08 kg
                    # Tvískráð
                    q = AthlAfrek.objects.all().filter(Q(tákn_greinar__iexact="LÓÐ9,08K") | Q(tákn_greinar__iexact="LÓÐ99,08K"))
                case 184: # Lóðkast 7,26 kg
                    # !
                    q = AthlAfrek.objects.all().filter(Q(tákn_greinar__iexact="LÓÐ7,26K"))
                case 185: # Lóðkast 5,45 kg
                    # Tvískráð
                    q = AthlAfrek.objects.all().filter(Q(tákn_greinar__iexact="LÓÐ5,45K") | Q(tákn_greinar__iexact="LÓÐ55,45K"))
                case _: # Default case
                    q = AthlAfrek.objects.all().filter(grein__iexact=Event_Info['THORID_2'], tákn_greinar__iexact=Event_Info['THORID_1'])

    #--
    if (Event_Info['Minimize'] == True):
        #order_by_str = 'árangur'
        if (Legal == 1):
            # Gagnagrunurinn er með dálk sem heitir löglegt. En það virðist ekki vera hægt að treysta honum.
            # Ólögleigir árangrar eru flokkaðir sem vindur > 2.0, vantar vind og/eða handtímataka
            #if (Event_Info['Units'] == 2): # Eining er sek, sem sagt spretthlaup þá viljum við rafmagnstíma
            #    electime = 1
            #    q = q.filter(rafmagnstímataka=electime)
            if (Event_Info['HasWind'] == True):
                q = q.filter(vindur__lte=2.00, vantar_vind=0)
            #q = q.filter(vindur__lte=2.00, vantar_vind=0)
    else: # Dálkurinn með rafmagnstímataka getur verið hvað sem er í greinum sem eru ekki með tímatöku.
        if (Legal == 1):
            if (Event_Info['HasWind'] == True):
                q = q.filter(vindur__lte=2.00, vantar_vind=0)

    #    order_by_str = '-árangur'

    q = q.filter(kyn=Gender, aldur_keppanda__range=[AgeStart, AgeEnd])

    if (IndoorOutDoor != 2): # 2 þýðir bæði úti og inni árangur
        q = q.filter(úti_inni=IndoorOutDoor)

    # Ef við viljum fá öll gögn þá er Year = 0
    #if (Year > 0):
    #    q = q.filter(dagsetning__gte=datetime.datetime(Year, 1, 1, tzinfo=pytz.UTC),
    #                 dagsetning__lte=datetime.datetime(Year, 12, 31, tzinfo=pytz.UTC))
    q = q.filter(dagsetning__gte=datetime.datetime.strptime(fromDate, '%Y-%m-%d'),
                 dagsetning__lte=datetime.datetime.strptime(toDate, '%Y-%m-%d'))

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

    return Achievements_list[:N], Event_Info

def Top_List():
    Top_Women = []
    Top_Men = []

    Event_Type = [3, 4, 3, 4, 3, 3, 4,
                  5, 5, 5, 5, 6, 3, 3, 5, # Hlaup og grind
                  1, 1, 1, 1, # Stökk
                  2, 2, 2, 2, # Köst
                  7, 7 # Þraut
                  ]

    Women_Events = [82, 86, 6, 7, 27, 48, 52,
                    97, 4, 19, 30, 62, 55, 59, 32, # Hlaup
                    179, 252, 143, 239, # Stökk
                    227, 168, 216, 154, # Köst
                    1001, 1011 # Þraut
                    ] 
    Men_Events   = [82, 83, 6, 15, 27, 48, 49,
                    97, 4, 19, 30, 62, 55, 59, 32, # Hlaup
                    179, 252, 143, 239, # Stökk
                    226, 162, 212, 152, # Köst
                    1011, 1021 # Þraut
                    ]

    # Get current year and set fromDate and toDate to cover whole year
    current_year = datetime.datetime.now().year
    fromDate = datetime.datetime(current_year, 1, 1).strftime('%Y-%m-%d')
    toDate = datetime.datetime(current_year, 12, 31).strftime('%Y-%m-%d')
    #current_year = 2020

    # -- Women
    for event_id, event_t in zip(Women_Events, Event_Type):
        Top_W, Event_info_W = Top_100_List(event_id, fromDate, toDate, 2, 2, 0, 99, True, 0, True, 1)

        try:
            # if (Top_W[0]['electronic_timing'] == 1):
            #     ElecTime = True
            # else:
            #     ElecTime = False
            Top_Women.append({'Name'          : Top_W[0]['name'],
                              'CompetitorID'  : Top_W[0]['competitor_code'],
                              #'Results'       : common.results_to_str(float(Top_W[0]['results']), Event_info_W['Units'], ElecTime),
                              'Results'       : Top_W[0]['results'],
                              'OutInn'        : Top_W[0]['outdoor_indoor'],
                              'Club'          : Top_W[0]['club'],
                              'EventName'     : Event_info_W['ShortName'],
                              'EventID'       : event_id,
                              'EventType'     : event_t,
                              'Units_symbol'  : Event_info_W['Units_symbol']
                              })
        except IndexError: # Index error þýðir líklegast að engin árangur fannst
            pass

    # -- Men
    for event_id, event_t in zip(Men_Events, Event_Type):
        Top_M, Event_info_M = Top_100_List(event_id, fromDate, toDate, 2, 1, 0, 99, True, 0, True, 1)

        try:
            # if (Top_M[0]['electronic_timing'] == 1):
            #     ElecTime = True
            # else:
            #     ElecTime = False
            Top_Men.append({'Name'          : Top_M[0]['name'],
                            'CompetitorID'  : Top_M[0]['competitor_code'],
                            #'Results'       : common.results_to_str(float(Top_M[0]['results']), Event_info_M['Units'], ElecTime),
                            'Results'       : Top_M[0]['results'],
                            'OutInn'        : Top_M[0]['outdoor_indoor'],
                            'Club'          : Top_M[0]['club'],
                            'EventName'     : Event_info_M['ShortName'],
                            'EventID'       : event_id,
                            'EventType'     : event_t,
                            'Units_symbol'  : Event_info_M['Units_symbol']
                            })
        except IndexError: # Index error þýðir líklegast að engin árangur fannst
            pass

    return Top_Women, Top_Men

def Get_Club_List():
    df_clubs = pd.read_csv(CLUB_LIST_FILENAME)
    list_of_clubs = []
    for index, row in df_clubs.iterrows():
        club_info = {'ShortName': row['shortname'],
                     'FullName': row['fullname'],
                     'ThorID': row['thorid']}
        list_of_clubs.append(club_info)

    return list_of_clubs

def Get_Club_List_Thor():
    club_data = pd.read_sql_query("EXEC ClubsForUser @UserLogin=''", connection)

    club_list = []
    for index, row in club_data.iterrows():
        club_list.append({'id': index,
                          'thorId': row.Club,
                          'fullName': row.NameOfClub,
                          'region': row['Héraðssamband']})
    return club_list

def Get_Competitor_List(s, club, startsWith, yob):

    #names_q = Competitors.objects.using('competitor_list').all()
    names_q = AthlCompetitors.objects.all()
    if (startsWith is not None):
        names_q = names_q.filter(Q(nafn__startswith=startsWith))

    if (club is not None):
        names_q = names_q.filter(Q(félag__icontains=club))

    if ((yob is not None) and (yob.isdigit() == True)):
        names_q = names_q.filter(Q(fæðingarár__icontains=yob))
        
    
    if (club is None and startsWith is None and yob is None):
        for i in s.split(' '):
            if (len(i) >= 2):
                if (i.isdigit() == True): # Athuga hvort þetta er tala
                    if (len(i) == 4): # Ef 4 stafa þá túlkum við þetta sem fæðingarár annars hunsum við.
                        names_q = names_q.filter(Q(fæðingarár__icontains=i))
                else:
                    names_q = names_q.filter(Q(nafn__icontains=i) | Q(félag__icontains=i))
    else:
        for i in s.split(' '):
            if (len(i) >= 2):
                names_q = names_q.filter(Q(nafn__icontains=i))

    #names_q = names_q.filter(Q(nafn__icontains=q) | Q(félag__icontains=q) | Q(fæðingarár__icontains=q) )

    results = []

    df = pd.DataFrame.from_records(names_q.values_list('númer', 'nafn', 'fæðingarár', 'félag', 'dags_síðast_uppfært'),
                                              columns=['keppandanúmer', 'nafn', 'fæðingarár', 'félag', 'dagsetning'])

    #df = pd.DataFrame.from_records(names_q.values_list('keppandanúmer', 'nafn', 'fæðingarár', 'félag', 'dagsetning'),
    #                                          columns=['keppandanúmer', 'nafn', 'fæðingarár', 'félag', 'dagsetning'])

    df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)
    df.sort_values(by=['dagsetning'], ascending=[False], inplace=True)

    #df.drop_duplicates(subset=['keppandanúmer'], keep='first', inplace=True, ignore_index=True)

    # Hendum út öllu nema í top 25 matches
    df = df.iloc[0:25]

    for index, row in df.iterrows():
        Competitor_Info = {'CompetitorCode': row.keppandanúmer,
                           'Name': row.nafn,
                           'FirstName': row.nafn.split(' ')[0],
                           'LastName': row.nafn.split(' ')[-1],
                           'YOB': row.fæðingarár,
                           'Club': row.félag
                           }
        results.append(Competitor_Info)

    return results

def Get_Competitor_Event_Data_All(CompetitorCode, Event_id):
    EventInfo = events.Get_Event_Info_by_ID(Event_id)
    df = competitor.Get_Competitor_Event_DataFrame(CompetitorCode, Event_id, EventInfo)

    EventData = []
    for index, row in df.iterrows():
        EventData.append({'strResults': row['árangur_str'],
                          'floatResults': row['árangur_float'],
                          'strWind': row['vindur_str'],
                          'Club': row['félag'],
                          'OutIn': row['úti_inni'],
                          'CompetitionName': row['heiti_móts'],
                          'CompetitionID': row['mót'],
                          'Age': row['aldur_keppanda'],
                          'Date': row['dagsetning'],
                          'ElectricTiming': row['rafmagnstímataka'],
                          'MissingWind': row['vantar_vind']
                         })
    return EventData