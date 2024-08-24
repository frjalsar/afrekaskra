# run python manage.py shell
# Then exec(open('Tests/Get_KT_Top.py').read())

from django.test import Client
import os
import pyodbc
import numpy as np
import pandas as pd

#from Sif import data

from Sif import common
from Sif import events

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors
from django.db.models import Q
from django.db import connection

Event_Type = [3, 4, 3, 4, 3, 3, 4,
              5, 5, 5, 6, 3, 3, 5,  # Hlaup og grind
              1, 1, 1, 1,  # Stökk
              2, 2, 2, 2,  # Köst
              7, 7  # Þraut
              ]

Women_Events = [82, 86, 6, 7, 27, 48, 52,
                97, 19, 30, 62, 55, 59, 32,  # Hlaup
                179, 252, 143, 239,  # Stökk
                227, 168, 216, 154,  # Köst
                1001, 1011  # Þraut
                ]
Men_Events = [82, 83, 6, 15, 27, 48, 49,
              97, 19, 30, 62, 55, 59, 32,  # Hlaup
              179, 252, 143, 239,  # Stökk
              226, 162, 212, 152,  # Köst
              1011, 1021  # Þraut
              ]

def Convert_Achievements_to_List_PD(q, best_by_ath, Event_Info):
    df = pd.DataFrame.from_records(q.values_list('lína', 'nafn', 'keppandanúmer',
                                                 'árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni', 'kennitala'),
                                                 columns=['lína', 'nafn', 'keppandanúmer',
                                                          'árangur', 'vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni', 'kennitala'])

    df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['árangur_float'] = df['árangur'].map(common.results_to_float)

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
    return df

def Top_100_List(Event_id, Year, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal, ISL, BestByAth, N=100):
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
                      'HasWind': 0}
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

    return Achievements_list[:N]

print('Women')
df_women = []
for event_id, event_t in zip(Women_Events, Event_Type):
    print(event_id)
    df_women.append(Top_100_List(event_id, 0, 2, 2, 0, 99, True, 0, True, 100))

df_w = pd.concat(df_women)
df_w.drop_duplicates(subset=['kennitala'], inplace=True)

df_w.to_csv("top_women.csv")

print('')
print('Men')
df_men = []
for event_id, event_t in zip(Men_Events, Event_Type):
    print(event_id)
    df_men.append(Top_100_List(event_id, 0, 2, 1, 0, 99, True, 0, True, 100))

df_m = pd.concat(df_men)
df_m.drop_duplicates(subset=['kennitala'], inplace=True)

df_m.to_csv("top_men.csv")