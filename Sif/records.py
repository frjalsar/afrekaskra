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
import datetime as dt
import pandas as pd

def Get_Records_Birthdays():
    q = AthlMetaskrFr.objects.all().filter(virkt__iexact=1).filter(Q(aldursflokkur_frí__iexact='KO') | Q(aldursflokkur_frí__iexact='KA'))

    df = pd.DataFrame.from_records(q.values_list('lína', 'línunr_í_afrekum', 'grein',
                                                 'kyn', 'dagsetning_mets', 'árangur',
                                                 'vindur', 'methafi', 'heiti_methafa',
                                                 'félag_methafa', 'staður_mets', 'úti_inni',
                                                 'aldur_methafa'),
                                                 columns=['Lína', 'Línunr_í_afrekum', 'Grein',
                                                          'Kyn', 'Dagsetning mets', 'Árangur',
                                                          'Vindur', 'Methafi', 'Heiti methafa',
                                                          'Félag methafa', 'Staður mets', 'Úti_Inni',
                                                          'Aldur methafa'])

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

    for index, row in result.head(n=10).iterrows():
        record_age = row['Record_age']
        if (record_age == 0): # Metið var sett í ár en afmælið er á næsta ári.
            record_age = 1

        List_of_Records.append({'Event': row['Grein'],
                               'Sex': row['Kyn'],
                               'Name': row['Heiti methafa'],
                               'Club': row['Félag methafa'],
                               'Place': row['Staður mets'],
                               'Inout': row['Úti_Inni'],
                               'Age_holder': row['Aldur methafa'],
                               'Age_record': record_age,
                               'Date': row['Dagsetning mets'],
                               'Day': row['Day'],
                               'Month': row['Month'],
                               'Year': row['Year']
                               })

    return List_of_Records

def Get_Competitor_Records(CompetitorCode):
    q = AthlMetaskrFr.objects.all().filter(methafi__iexact=CompetitorCode).order_by('aldursflokkur_frí', 'dagsetning_mets')

    record_list = []
    for record in q:
        wind_str = '{:+.1f}'.format(float(record.vindur))
        results = common.results_to_float(record.árangur.replace(',', '.'))
        results_str = record.árangur
        date_str = format_date(record.dagsetning_mets.date(), "d MMM yyyy", locale='is_IS').upper()
        active = record.virkt
        age = record.aldur_methafa
        agegroup = record.aldursflokkur_frí
        inout = record.úti_inni
        club = record.félag_methafa
        event = record.grein

        record_info = {'Event': event,
                       'Club': club,
                       'Inout': inout,
                       'AgeGroup': agegroup,
                       'Age': age,
                       'isActive': active,
                       'Date': date_str,
                       'Results': results,
                       'Results_str': results_str,
                       'Wind': wind_str
                      }

        record_list.append(record_info)

    return record_list