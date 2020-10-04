from Sif import common
from Sif import events
import numpy as np
import pandas as pd
from datetime import datetime

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors
from django.db.models import Q
from django.db import connection

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
                           'FirstName': q.nafn.split(' ', 1)[0],
                           'LastName': q.nafn.split(' ', 1)[-1],
                           'YOB': q.fæðingarár,
                           'Club': q.félag,
                           'Sex': q.kyn
                           }
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info

def Get_Competitor_Achievements(CompetitorCode):
    # Núverandi ár. Þarf til að kalla á stored procedure
    CurrentYear = datetime.now().year
    
    # Köllum á stored procedure sem heitir CompetitorsAchievements.
    df = pd.read_sql_query("EXEC CompetitorsAchievements @CompetitorNo = {:d}, @YearFrom = 1800, @YearTo = {:d}, @OutdoorsIndoorsFilter = '%'".format(CompetitorCode, CurrentYear), connection)

    # Breytum öllum árangri yfir í rauntölur
    df['Results_float'] = df['Results'].map(common.results_to_float)
    return df

def Get_Competitor_Events_Info(CompetitorCode):
    df = Get_Competitor_Achievements(CompetitorCode)

    # Búa til lista yfir greinar
    list_events = df.copy() # copy til að búa til afrit
    list_events.drop_duplicates(subset=['EventName'], inplace=True) # Henda út endurtekningum
    list_events.reset_index(drop=True, inplace=True) # Endur númera index
    print(list_events)

    list_pb = []
    list_sb = []
    for index, row in list_events.iterrows():
        #try:
        event_info = events.Get_Event_Info_by_Name(row['EventName'])
        #except:
        #    print('Hello')
        #    continue

        # Flokka út Grein
        df_event = df.loc[df['EventName'] == row['EventName']].copy() # Búum til copy til að breyta
        df_event.reset_index(drop=True, inplace=True) # Endur númera index

        # Úti árangur með löglegum vindi
        mask = np.logical_and(df_event['WindReading'] <= 2.0, df_event['OutdoorsOrIndoors'] == 'Úti')
        #mask = np.logical_and(mask, df_event['vantar_vind'] == 0)
        df_event_nowind_out = df_event.loc[mask]

        df_event_out = df_event.loc[df_event['OutdoorsOrIndoors'] == 'Úti'] # Úti árangur + vind árangur
        df_event_in = df_event.loc[df_event['OutdoorsOrIndoors'] == 'Inni'] # Inni árangur

        #print(df_event_out.head(n=10))

        # Telja hve oft viðkomandi hefur keppt í þessari grein
        count = df_event['Results'].count()

        pb_out = ''
        pb_out_date = datetime(1970, 1, 1)

        pb_in = ''
        pb_in_date = datetime(1970, 1, 1)

        #try:
            # Finnum PB inni ef það er til
        if (df_event_in.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_in['Results_float'].idxmax()
            else:
                idx = df_event_in['Results_float'].idxmin()

            pb_in = df_event_in['Results'][idx]
            pb_in_date = df_event_in['AchievementDate'][idx]

        # Finnum PB úti með löglegum árangri ef það er til
        if (df_event_nowind_out.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_nowind_out['Results_float'].idxmax()
            else:
                idx = df_event_nowind_out['Results_float'].idxmin()

            pb_out = df_event_nowind_out['Results'][idx]
            pb_out_date = df_event_nowind_out['AchievementDate'][idx]

        # Ef ekki þá athugum við ólöglegan árangur
        elif (df_event_out.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_out['Results_float'].idxmax()
            else:
                idx = df_event_out['Results_float'].idxmin()

            pb_out = df_event_out['Results'][idx] + ' ({:+.1f}'.format(df_event_out['WindReading'][idx]) + ' m/s)'
            pb_out_date = df_event_out['AchievementDate'][idx]
        #except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
        #    pass

        date_now = datetime.today()
        date_from_cur = np.datetime64(datetime(date_now.year, 1, 1, 0, 0, 0)) # 1 jan þessi ári
        date_to_cur = np.datetime64(date_now) # Í dag

        date_from_last = np.datetime64(datetime(date_now.year-1, 1, 1, 0, 0, 0)) # 1 jan á seinasta ári
        date_to_last = np.datetime64(datetime(date_now.year-1, 12, 31, 0, 0, 0)) # 31 des á seinasta ári

        # Árangur með löglegum vindi
        mask = df_event['WindReading'] <= 2.0
        df_event_nowind = df_event.loc[mask]

        #print(type(date_now))
        #print(df_event.dtypes)

        # Þetta ár
        #mask_cur = np.logical_and(df_event['dagsetning'] < date_to_cur, date_from_cur < df_event['dagsetning'])
        df_event_sb_cur = df_event.loc[df_event['AchievementDate'].dt.year == 2020]
        #print(df_event_sb_cur)
        #if (df_event_sb_cur.empty == False):
        #    print(df_event_sb_cur)

        # Þetta ár löglegur vindur
        #mask_cur_nowind = np.logical_and(df_event_nowind['dagsetning'] < date_to_cur, date_from_cur < df_event_nowind['dagsetning'])
        df_event_nowind_sb_cur = df_event_nowind.loc[df_event['AchievementDate'].dt.year == date_now.year]

        # Fyrra
        #mask_last = np.logical_and(df_event['dagsetning'] < date_to_last, date_from_last <=df_event['dagsetning'])
        df_event_sb_last = df_event.loc[df_event['AchievementDate'].dt.year == (date_now.year-1)]

        # Í fyrra löglegur árangur
        #mask_last_nowind = np.logical_and(df_event_nowind['dagsetning'] < date_to_last, date_from_last < df_event_nowind['dagsetning'])
        df_event_nowind_sb_last = df_event_nowind.loc[df_event['AchievementDate'].dt.year == (date_now.year-1)]

        sb_cur = ''
        try:
            # Finnum SB inni ef það er til
            if (df_event_nowind_sb_cur.empty == False):
                #print(df_event_nowind_sb_cur)
                if (event_info['MAX'] == True):
                    idx = df_event_nowind_sb_cur['Results_float'].idxmax()
                else:
                    idx = df_event_nowind_sb_cur['Results_float'].idxmin()
                    
                sb_cur = df_event_nowind_sb_cur['Results'][idx]
                #print(sb_cur)

                # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_cur.empty == False):
                if (event_info['MAX'] == True):
                    idx = df_event_sb_cur['Results_float'].idxmax()
                else:
                    idx = df_event_sb_cur['Results_float'].idxmin()
                    
                wind_str = '{:+.1f}'.format(df_event_sb_cur['WindReading'][idx])
                sb_cur = df_event_sb_cur['Results'][idx] + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
        #    sub_cur = ''
            pass

        sb_last = ''
        try:
            # Finnum SB úti með löglegum árangri ef það er til
            if (df_event_nowind_sb_last.empty == False):
                if (event_info['MAX'] == True):
                    idx = df_event_nowind_sb_last['Results_float'].idxmax()
                else:
                    idx = df_event_nowind_sb_last['Results_float'].idxmin()

                sb_last = df_event_nowind_sb_last['Results'][idx]

            # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_last.empty == False):
                if (event_info['MAX'] == True):
                    idx = df_event_sb_last['Results_float'].idxmax()
                else:
                    idx = df_event_sb_last['Results_float'].idxmin()

                wind_str = '{:+.1f}'.format(df_event_sb_last['WindReading'][idx])
                sb_last = df_event_sb_last['Results'][idx] + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
            #print('Error')
            #sb_last = ''
            pass

        # Bæta við í listan
        list_pb.append({'EventName': row['EventName'],
                        'EventShortName': event_info['NAME_SHORT'],
                        'EventUnit': event_info['UNIT_SYMBOL'],
                        'EventID': event_info['EVENT_ID'],
                        'PB_out': pb_out,
                        'PB_out_date': pb_out_date.year,
                        'PB_in': pb_in,
                        'PB_in_date': pb_in_date.year,
                        'SB_cur': sb_cur,
                        'SB_last': sb_last,
                        'count': int(count)
                        })

    # Röðum listanum í öfuga röð eftir því oft hefur verið keppt í greinunum
    # Þarf ekki því html taflan gerir þetta líka!!
    list_pb.sort(key=lambda dic: dic['count'], reverse=True)

    print(list_pb)

    return list_pb


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