from Sif import common
import pandas as pd

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors
from django.db.models import Q

# Skilar til baka Pandas data frame með öllum upplýsingum um ákveðna grein fyrir einhvern keppanda.
def Get_Competitor_Event_DataFrame(CompetitorCode, Event_id, EventInfo):

    # Náum í gögn úr Þór
    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode, tákn_greinar__iexact=EventInfo['THORID_1']).order_by('dagsetning')

    # Búum til Pandas dataframe
    df = pd.DataFrame.from_records(q.values_list('árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                 'grein', 'tákn_greinar', 'vantar_vind'),
                                                 columns=['árangur', 'vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                          'grein', 'tákn_greinar', 'vantar_vind'])

    #df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Búum til tóma dálka
    df['árangur_float'] = 0.0
    df['árangur_str'] = ''
    df['vindur_str'] = ''

    for index, row in df.iterrows():
        # Breytum öllum árangri yfir í rauntölur
        results_float = common.results_to_float(row['árangur'])
        df.iloc[index, df.columns.get_loc('árangur_float')] = results_float

        # Breytum vind yfir í string með + eða -
        if (row['vantar_vind'] == True):
            wind_str = 'N/A'
        else:
            wind_str = common.wind_to_str(row['vindur'])
        df.iloc[index, df.columns.get_loc('vindur_str')] = wind_str

        # Breytum árangri yfir í string
        if (row['rafmagnstímataka'] == 0 and EventInfo['Minimize'] == True):
            result_str = '{:.1f}'.format(results_float)
        else:
            if (EventInfo['Units'] == 5):
                result_str = '{:.0f}'.format(results_float)
            else:
                result_str = '{:.2f}'.format(results_float)

        df.iloc[index, df.columns.get_loc('árangur_str')]

    print(df['árangur_float'])
    return df