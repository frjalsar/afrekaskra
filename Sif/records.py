from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors, AthlMetaskrFr
from django.db.models import Q

# Settings
from Sif import settings

from babel.dates import format_date, format_datetime, format_time
from Sif import common
from Sif import events
import datetime as dt
import pandas as pd
from django.db import connection

def Get_Records_Birthdays():
    #q = AthlMetaskrFr.objects.all().filter(virkt__iexact=1) #.filter(Q(aldursflokkur_frí__iexact='KO') | Q(aldursflokkur_frí__iexact='KA'))

    #df = pd.DataFrame.from_records(q.values_list('lína', 'línunr_í_afrekum', 'grein',
    #                                             'kyn', 'dagsetning_mets', 'árangur',
    #                                             'vindur', 'methafi', 'heiti_methafa',
    #                                             'félag_methafa', 'staður_mets', 'úti_inni',
    #                                             'aldur_methafa', 'aldursflokkur_frí'),
    #                                             columns=['Lína', 'Línunr_í_afrekum', 'Grein',
    #                                                      'Kyn', 'Dagsetning mets', 'Árangur',
    #                                                      'Vindur', 'Methafi', 'Heiti methafa',
    #                                                      'Félag methafa', 'Staður mets', 'Úti_Inni',
    #                                                      'Aldur methafa', 'Aldursflokkur'])

    df = pd.read_sql_query("EXEC Islandsmet", connection)

    df = df.astype({"KrefsVindm": bool, "ÚtiInni": int})
    df['Dagsetn'] = pd.to_datetime(df['Dagsetn'], yearfirst=True)

    df['Day'] = df['Dagsetn'].dt.day
    df['Month'] = df['Dagsetn'].dt.month
    df['Year'] = df['Dagsetn'].dt.year

    month = dt.datetime.now().month
    day = dt.datetime.now().day
    year = dt.datetime.now().year

    df['Record_age'] = year - df['Year']

    df.sort_values(by=['Month', 'Day'], inplace=True)
    df_month = df.loc[df['Month'] >= month]
    df_filter = df_month.loc[df_month['Day'] >= day]
    result = pd.concat([df_filter, df]).reset_index()

    List_of_Records = []

    if (dt.date.today().month == 12) and (dt.date.today().day >= 28):
        N = 85 # Rosalega mörg met sem eru sett 30 og 31. des
    else:
        N = 15 # Vanalega er 15 nóg

    for index, row in result.head(n=N).iterrows():
        record_age = row['Record_age']
        if (record_age == 0): # Metið var sett í ár en afmælið er á næsta ári.
            record_age = 1


        inout = row['ÚtiInni']
        wind_str = row['Vindur']  #common.wind_to_str(row['Vindur'], inout, row['KrefsVindm'])
        results_str = row['Arangur']
        results = common.results_to_float(results_str.replace(',', '.'))
        date_str = format_date(row['Dagsetn'].date(), "d MMM yyyy", locale='is_IS').upper()
        agegroup = row['AldursflFRÍ']
        club = row['Félag']

        event_info = events.Get_Event_Info_by_Name(row['HeitiGreinar'])
        EventShorterName = row['HeitiGreinar'].replace('metra', 'm').replace('boðhlaup', 'bh.').replace('hlaup', '').replace('grind', 'gr.').replace('atrennu', 'atr.')
        event = EventShorterName
        units = event_info['UNIT']
        units_symbol = event_info['UNIT_SYMBOL']
        competitorid = row['Keppandan']

        # Nafnið kemur með ártalinu í lokinn. Klippum það út.
        name = row['Nafn'].rsplit(' ', 1)[0]

        List_of_Records.append({'Event': event,
                               'Results': results,
                               'Results_str': results_str,
                               'Wind': wind_str,
                               'Sex': row['Ky'],
                               'Name': name,
                               'Club': club,
                               'Place': row['Staður'],
                               'Inout': inout,
                               'Age_record': record_age,
                               'AgeGroup': agegroup,
                               'Date': date_str,
                               'Day': row['Day'],
                               'Month': row['Month'],
                               'Year': row['Year'],
                               'Units': units,
                               'Units_symbol': units_symbol,
                               'CompetitorID': competitorid
                               })

    return List_of_Records

def Get_Competitor_Records(CompetitorCode):
    #q = AthlMetaskrFr.objects.all().filter(methafi__iexact=CompetitorCode).order_by('aldursflokkur_frí', 'dagsetning_mets')

    now = dt.datetime.now()
    df = pd.read_sql_query("EXEC CompetitorsRecords @CompetitorNo = '{:d}', @YearFrom = 1800, @YearTo = {:d}, @OutdoorsIndoorsFilter = '%'".format(CompetitorCode, now.year), connection)
    df['AchievementDate'] = pd.to_datetime(df['AchievementDate'], yearfirst=True)

    record_list = []
    for index, row in df.iterrows():
        if (row['OutdoorsOrIndoors'] == 'Inni'):
            inout = 1
        else:
            inout = 0
        wind_str = row['WindReading']
        results_str = row['Results']
        results = common.results_to_float(results_str.replace(',', '.'))
        date_str = format_date(row['AchievementDate'].date(), "d MMM yyyy", locale='is_IS').upper()
        if (row['ActiveText'] == 'Virkt'):
            active = True
        else:
            active = False
        age = row['Age']
        agegroup = row['AgeGroup']
        club = row['Club']

        event_info = events.Get_Event_Info_by_Name(row['EventName'])
        EventShorterName = row['EventName'].replace('metra', 'm').replace('boðhlaup', 'bh.').replace('hlaup', '').replace('grind', 'gr.').replace('atrennu', 'atr.')
        event = EventShorterName
        units = event_info['UNIT']
        units_symbol = event_info['UNIT_SYMBOL']

        record_info = {'Event': event,
                       'Club': club,
                       'Inout': inout,
                       'AgeGroup': agegroup,
                       'Age': age,
                       'isActive': active,
                       'Date': date_str,
                       'Results': results,
                       'Results_str': results_str,
                       'Wind': wind_str,
                       'Units': units,
                       'Units_symbol': units_symbol
                      }

        record_list.append(record_info)

    return record_list