from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
#from Sif.models import AthlCompetitors, AthlAfrek, Competitors, AthlMetaskrFr
#from django.db.models import Q

# Settings
#from Sif import settings

from babel.dates import format_date #, format_datetime, format_time
from Sif import common
from Sif import events
from Sif import competitor
import datetime as dt
from dateutil.relativedelta import *
import pandas as pd
from django.db import connection
import threading

import warnings
warnings.filterwarnings('ignore')

# Return all Icelandic records in all agegroups.
#['KA', 'PI22', 'PI19', 'PI17', 'PI15', 'PI14', 'PI13', 'PI12']
#['KO', 'ST22', 'ST19', 'ST17', 'ST15', 'ST14', 'ST13', 'ST12']
def Get_All_National_Records():
    df = pd.read_sql_query("EXEC Islandsmet", connection)

    df = df.astype({"KrefsVindm": bool,
                    "ÚtiInni": int
                   })
    df['Dagsetn'] = pd.to_datetime(df['Dagsetn'], yearfirst=True)

    df['Day'] = df['Dagsetn'].dt.day
    df['Month'] = df['Dagsetn'].dt.month
    df['Year'] = df['Dagsetn'].dt.year

    return df

def Get_All_Master_Records():
    def fetch_data(query, connection, result_list, index):
        result_list[index] = pd.read_sql_query(query, connection)

    # Queries
    queries = [
        "EXEC Oldungamet2 @OutdoorsIndoors = 1, @KarlarKonur = 1, @SelectedCompetitorCode = NULL",
        "EXEC Oldungamet2 @OutdoorsIndoors = 0, @KarlarKonur = 1, @SelectedCompetitorCode = NULL",
        "EXEC Oldungamet2 @OutdoorsIndoors = 1, @KarlarKonur = 2, @SelectedCompetitorCode = NULL",
        "EXEC Oldungamet2 @OutdoorsIndoors = 0, @KarlarKonur = 2, @SelectedCompetitorCode = NULL"
    ]

    # List to store results
    results = [None] * len(queries)

    # Create and start threads
    threads = []
    for i, query in enumerate(queries):
        thread = threading.Thread(target=fetch_data, args=(query, connection, results, i))
        threads.append(thread)
        thread.start()

    # Join threads
    for thread in threads:
        thread.join()

    # Concatenate results
    df = pd.concat(results)

    # df_men_in = pd.read_sql_query("EXEC Oldungamet2 @OutdoorsIndoors = 1, @KarlarKonur = 1, @SelectedCompetitorCode = NULL", connection)
    # df_men_out = pd.read_sql_query("EXEC Oldungamet2 @OutdoorsIndoors = 0, @KarlarKonur = 1, @SelectedCompetitorCode = NULL", connection)

    # df_women_in = pd.read_sql_query("EXEC Oldungamet2 @OutdoorsIndoors = 1, @KarlarKonur = 2, @SelectedCompetitorCode = NULL", connection)
    # df_women_out = pd.read_sql_query("EXEC Oldungamet2 @OutdoorsIndoors = 0, @KarlarKonur = 2, @SelectedCompetitorCode = NULL", connection)
    
    # df = pd.concat([df_men_in, df_men_out, df_women_in, df_women_out])
    
    df = df.astype({"ÚtiInni": int})
    df['Dags'] = pd.to_datetime(df['Dags'], yearfirst=True)
    
    df['Day'] = df['Dags'].dt.day
    df['Month'] = df['Dags'].dt.month
    df['Year'] = df['Dags'].dt.year
    #print('Master records fetched')
    return df

def Get_Records_Birthdays():
    df = Get_All_National_Records()

    date_now = dt.datetime.now()
    #date_now = dt.date(2021, 12, 28) # Test date for debug

    month = date_now.month
    day = date_now.day
    year = date_now.year

    future = date_now + relativedelta(months=+1) # Framtíðin er +1 mánuður
    future_month = future.month
    future_day = future.day

    # Reiknar aldur meta
    df['Record_age'] = year - df['Year']

    # Ná öll met sem er í á milli dagsetningar í dag og framtíðar (+1 mánuður)
    df_filter = df.loc[((df['Month'] == month) & (df['Day'] >= day)) | ((df['Month'] == future_month) & (df['Day'] < future_day))]
    
    # Röðum eftir dagsetningu.
    # Athuga að röðin þarf að vera öfug fyrir mánuð í desember því annars kemur janúar á undan.
    if (month == 12):
        df_filter = df_filter.sort_values(by=['Month', 'Day'], ascending=[False, True]).reset_index()
    else:
        df_filter = df_filter.sort_values(by=['Month', 'Day'], ascending=[True, True]).reset_index()

    # Búa til listann yfir met til að senda sem json
    List_of_Records = []

    for index, row in df_filter.iterrows():
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

        if (row['HeitiGreinar'] == None): # Vantar HeitiGreinar á sum íslandsmet í töflunni. ÞARF AÐ LAGA
            continue
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

    Competitor_info = competitor.Get_Competitor_Info(CompetitorCode)

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

        try:
            event_info = events.Get_Event_Info_by_Name(row['EventName'])
        except:
            continue

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

        
    # Athuga hvort keppandi sé 30+ og hvort það þurfi að sækja 30+ met
    if (dt.datetime.now().year - Competitor_info['YOB']  >= 30):
        # Ná í 30+ met
        # Það þarf að kalla á SQL procedure fyrir kyn og fyrir innan og utan hús.
        df_master_in = pd.read_sql_query("EXEC OldungametKeppanda @CompetitorCode = {:d}, @OutdoorsIndoors = 1, @Gendr = {:d}".format(CompetitorCode, Competitor_info['Sex']), connection)
        df_master_out = pd.read_sql_query("EXEC OldungametKeppanda @CompetitorCode = {:d}, @OutdoorsIndoors = 0, @Gendr = {:d}".format(CompetitorCode, Competitor_info['Sex']), connection)

        df_master = pd.concat([df_master_in, df_master_out])
        df_master['Dags'] = pd.to_datetime(df_master['Dags'], yearfirst=True)

        for index, row in df_master.iterrows():
            inout = row['ÚtiInni']
            wind_str = row['Vindur']
            results_str = row['Árang']
            results = common.results_to_float(results_str.replace(',', '.'))
            date_str = format_date(row['Dags'].date(), "d MMM yyyy", locale='is_IS').upper()
            if (row['HeitiGr'] == None): # Vantar HeitiGreinar á sum íslandsmet í töflunni. ÞARF AÐ LAGA
                continue
            event_info = events.Get_Event_Info_by_Name(row['HeitiGr'])
            EventShorterName = row['HeitiGr'].replace('metra', 'm').replace('boðhlaup', 'bh.').replace('hlaup', '').replace('grind', 'gr.').replace('atrennu', 'atr.')
            event = EventShorterName
            units = event_info['UNIT']
            units_symbol = event_info['UNIT_SYMBOL']
            active = True
            age = row['Aldur keppanda']
            agegroup = row['Aldursflokkuröldunga']
            club = row['Félag']

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