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

def Get_Records_Birthdays():
    q = AthlMetaskrFr.objects.all().filter(virkt__iexact=1) #.filter(Q(aldursflokkur_frí__iexact='KO') | Q(aldursflokkur_frí__iexact='KA'))

    df = pd.DataFrame.from_records(q.values_list('lína', 'línunr_í_afrekum', 'grein',
                                                 'kyn', 'dagsetning_mets', 'árangur',
                                                 'vindur', 'methafi', 'heiti_methafa',
                                                 'félag_methafa', 'staður_mets', 'úti_inni',
                                                 'aldur_methafa', 'aldursflokkur_frí'),
                                                 columns=['Lína', 'Línunr_í_afrekum', 'Grein',
                                                          'Kyn', 'Dagsetning mets', 'Árangur',
                                                          'Vindur', 'Methafi', 'Heiti methafa',
                                                          'Félag methafa', 'Staður mets', 'Úti_Inni',
                                                          'Aldur methafa', 'Aldursflokkur'])

    df['Day'] = df['Dagsetning mets'].dt.day
    df['Month'] = df['Dagsetning mets'].dt.month
    df['Year'] = df['Dagsetning mets'].dt.year

    month = dt.datetime.now().month
    day = dt.datetime.now().day
    year = dt.datetime.now().year

    df['Record_age'] = year - df['Year']

    df.sort_values(by=['Month', 'Day'], inplace=True)
    df_month = df.loc[df['Month'] >= month]
    df_filter = df_month.loc[df_month['Day'] >= day]
    result = pd.concat([df_filter, df]).reset_index()

    List_of_Records = []

    for index, row in result.head(n=15).iterrows():
        record_age = row['Record_age']
        if (record_age == 0): # Metið var sett í ár en afmælið er á næsta ári.
            record_age = 1

        try:
            line_afrek = row['Línunr_í_afrekum']
            q_afrek = AthlAfrek.objects.get(pk=line_afrek) # Primary key (pk) er línu númerið
        except:
            print('VILLA FANN EKKI LÍNU FYRIR ÍSLANDSMET')
            print(line_afrek)
            print('')
        
        event_id = events.df_event_list[events.df_event_list['THORID_1'] == q_afrek.tákn_greinar].index.tolist()[0]
        event_info = events.Get_Event_Info(event_id)

        inout = row['Úti_Inni']
        wind_str = common.wind_to_str(row['Vindur'], inout, event_info['HasWind'])
        results = common.results_to_float(q_afrek.árangur.replace(',', '.'))
        results_str = q_afrek.árangur
        date_str = format_date(row['Dagsetning mets'].date(), "d MMM yyyy", locale='is_IS').upper()
        age = row['Aldur methafa']
        agegroup = row['Aldursflokkur']
        club = row['Félag methafa']
        event = event_info['ShortName']
        units = event_info['Units']
        units_symbol = event_info['Units_symbol']
        elec_time = q_afrek.rafmagnstímataka
        competitorid = q_afrek.keppandanúmer

        List_of_Records.append({'Event': event,
                               'Results': results,
                               'Results_str': results_str,
                               'Wind': wind_str,
                               'Sex': row['Kyn'],
                               'Name': row['Heiti methafa'],
                               'Club': club,
                               'Place': row['Staður mets'],
                               'Inout': inout,
                               'Age_holder': age,
                               'Age_record': record_age,
                               'AgeGroup': agegroup,
                               'Date': date_str,
                               'Day': row['Day'],
                               'Month': row['Month'],
                               'Year': row['Year'],
                               'Units': units,
                               'Units_symbol': units_symbol,
                               'Electronic_timing': elec_time,
                               'CompetitorID': competitorid
                               })

    return List_of_Records

def Get_Competitor_Records(CompetitorCode):
    q = AthlMetaskrFr.objects.all().filter(methafi__iexact=CompetitorCode).order_by('aldursflokkur_frí', 'dagsetning_mets')

    record_list = []
    for record in q:
        line_afrek = record.línunr_í_afrekum
        try:
            q_afrek = AthlAfrek.objects.get(pk=line_afrek) # Primary key (pk) er línu númerið
        except:
            print('VILLA FANN EKKI LÍNU FYRIR ÍSLANDSMET')
            print(line_afrek)
            print('')

        event_id = events.df_event_list[events.df_event_list['THORID_1'] == q_afrek.tákn_greinar].index.tolist()[0]
        event_info = events.Get_Event_Info(event_id)

        inout = record.úti_inni
        wind_str = common.wind_to_str(record.vindur, inout, event_info['HasWind'])
        results = common.results_to_float(q_afrek.árangur.replace(',', '.'))
        results_str = q_afrek.árangur
        date_str = format_date(record.dagsetning_mets.date(), "d MMM yyyy", locale='is_IS').upper()
        active = record.virkt
        age = record.aldur_methafa
        agegroup = record.aldursflokkur_frí
        club = record.félag_methafa
        line_afrek = record.línunr_í_afrekum
        event = event_info['ShortName']
        units = event_info['Units']
        units_symbol = event_info['Units_symbol']
        elec_time = q_afrek.rafmagnstímataka

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
                       'Units_symbol': units_symbol,
                       'Electronic_timing': elec_time
                      }

        record_list.append(record_info)

    return record_list