from Sif import common
from Sif import events
import numpy as np
import pandas as pd
#pd.options.mode.copy_on_write = True
pd.options.mode.chained_assignment = None  # default='warn'
from datetime import datetime, timedelta

import warnings
warnings.filterwarnings('ignore')

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors
from django.db.models import Q
from django.db import connection
from django.http import Http404

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
                           'Sex': q.kyn # 1 = Men, 2 = Women
                           }
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info


    # DECLARE @AchieveMents TABLE (
	# EventName nvarchar(100),
	# OutdoorsOrIndoors nvarchar(10),
	# Results nvarchar(20),
    # AchievementDate datetime,
	# Venue nvarchar(50),
	# Club nvarchar(20),
	# Age int,
	# WindReading decimal(38,1),
	# CompetitionName nvarchar(50),
	# CompetitionCode nvarchar(20),
	# Placing nvarchar(10),
	# Remarks nvarchar(200),
	# EventSortOrder decimal(38,20),
	# AchievementSortOrder decimal(30,20),
	# Series nvarchar(150),
	# RequiresWindMeter int,
	# WindReadingText nvarchar(20));
def Get_Competitor_Achievements(CompetitorCode):
    # Núverandi ár. Þarf til að kalla á stored procedure
    warnings.filterwarnings('ignore')
    CurrentYear = datetime.now().year
    
    # Köllum á stored procedure sem heitir CompetitorsAchievements.
    df = pd.read_sql_query("EXEC CompetitorsAchievementsSif @CompetitorNo = {:d}, @YearFrom = 1800, @YearTo = {:d}, @OutdoorsIndoorsFilter = '%'".format(CompetitorCode, CurrentYear), connection)

    # Athuga hvort það séu einhver afrek skráð
    # ATH það kemur ekki villa á front end þegar þetta gerist, bara tóma síða.
    if (df.empty):
        raise Http404('Engin afrek skráð á keppanda.')

    # Breytum öllum árangri yfir í rauntölur
    df['Results_float'] = df['Results'].map(common.results_to_float)

    # Breyta kommu í punkt
    df['EventName'] = df.EventName.str.replace(',', '.')
    return df

#def Get_Competitor_Events_Info(CompetitorCode):
def Get_Competitor_Events_Info(df, CompetitorCode=None):
    #df = Get_Competitor_Achievements(CompetitorCode)

    # Búa til lista yfir greinar
    list_events = df.copy() # copy til að búa til afrit
    list_events.drop_duplicates(subset=['EventName'], inplace=True) # Henda út endurtekningum
    list_events.reset_index(drop=True, inplace=True) # Endur númera index
    #print(list_events)

    list_pb = []
    list_sb = []
    for index, row in list_events.iterrows():
        try:
            event_info = events.Get_Event_Info_by_Name(row['EventName'])
        except:
            print('Error: Get_Event_Info_by_Name')
            #print(row['EventName'])
            print('index = {}'.format(index))
            print('competitor = {}'.format(CompetitorCode))
            print(row)
            continue

        # Flokka út Grein
        df_event = df.loc[df['EventName'] == row['EventName']].copy() # Búum til copy til að breyta
        df_event.reset_index(drop=True, inplace=True) # Endur númera index

        # Úti árangur með löglegum vindi
        mask = np.logical_and(df_event['WindReading'] <= 2.0, df_event['OutdoorsOrIndoors'] == 'Úti')
        #mask = np.logical_and(mask, df_event['vantar_vind'] == 0)
        df_event_nowind_out = df_event.loc[mask].copy()

        df_event_out = df_event.loc[df_event['OutdoorsOrIndoors'] == 'Úti'] # Úti árangur + vind árangur
        df_event_in = df_event.loc[df_event['OutdoorsOrIndoors'] == 'Inni'] # Inni árangur

        #print(df_event_out.head(n=10))

        # Telja hve oft viðkomandi hefur keppt í þessari grein
        count = df_event['Results'].count()

        pb_out = ''
        pb_out_date = datetime(1970, 1, 1)

        pb_in = ''
        pb_in_date = datetime(1970, 1, 1)

        # Bæta við buffer ef tíminn er handtími
        hand_buffer = common.Get_Hand_buffer(event_info['DISTANCE'])

        # Búum til nýjan dálk þar sem búið er að bæta við buffer tímanum.
        # Flokkum svo eftir þeim dálk.
        df_event_out['Results_sort'] = df_event_out['Results_float'].copy()
        for index, row in df_event_out.iterrows():
            if row['Rafmagnstímataka'] == 1:
                df_event_out.loc[index, 'Results_sort'] = row['Results_float']
            else:
                df_event_out.loc[index, 'Results_sort'] = row['Results_float'] + hand_buffer

        df_event_nowind_out['Results_sort'] = df_event_nowind_out['Results_float'].copy()
        for index, row in df_event_nowind_out.iterrows():
            if row['Rafmagnstímataka'] == 1:
                df_event_nowind_out.loc[index, 'Results_sort'] = row['Results_float']
            else:
                df_event_nowind_out.loc[index, 'Results_sort'] = row['Results_float'] + hand_buffer

        df_event_in['Results_sort'] = df_event_in['Results_float'].copy()
        #df_event_in['Results_sort'] = df_event_in.loc[:, 'Results_float']
        for index, row in df_event_in.iterrows():
            if row['Rafmagnstímataka'] == 1:
                df_event_in.loc[index, 'Results_sort'] = row['Results_float']
            else:
                df_event_in.loc[index, 'Results_sort'] = row['Results_float'] + hand_buffer

        #try:
            # Finnum PB inni ef það er til
        if (df_event_in.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_in['Results_sort'].idxmax()
            else:
                idx = df_event_in['Results_sort'].idxmin()

            if (df_event_in['Rafmagnstímataka'][idx] == 1):
                ElecTime = True
            else:
                ElecTime = False
            pb_in = common.results_to_str(df_event_in['Results_float'][idx], event_info['UNIT'], ElecTime, event_info['DISTANCE'])
            pb_in_date = df_event_in['AchievementDate'][idx]

        # Finnum PB úti með löglegum árangri ef það er til
        if (df_event_nowind_out.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_nowind_out['Results_sort'].idxmax()
            else:
                idx = df_event_nowind_out['Results_sort'].idxmin()

            if (df_event_nowind_out['Rafmagnstímataka'][idx] == 1):
                ElecTime = True
            else:
                ElecTime = False
            pb_out = common.results_to_str(df_event_nowind_out['Results_float'][idx], event_info['UNIT'], ElecTime, event_info['DISTANCE'])
            pb_out_date = df_event_nowind_out['AchievementDate'][idx]

        # Ef ekki þá athugum við ólöglegan árangur
        elif (df_event_out.empty == False):
            if (event_info['MAX'] == True):
                idx = df_event_out['Results_sort'].idxmax()
            else:
                idx = df_event_out['Results_sort'].idxmin()

            if (df_event_out['Rafmagnstímataka'][idx] == 1):
                ElecTime = True
            else:
                ElecTime = False
            pb_out = common.results_to_str(df_event_out['Results_float'][idx], event_info['UNIT'], ElecTime, event_info['DISTANCE']) + ' ({:+.1f}'.format(df_event_out['WindReading'][idx]) + ' m/s)'
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
        df_event_sb_cur = df_event.loc[df_event['AchievementDate'].dt.year == date_now.year]
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
                    
                sb_cur = common.results_to_str(df_event_nowind_sb_cur['Results_float'][idx], event_info['UNIT'], True, event_info['DISTANCE'])
                #print(sb_cur)

                # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_cur.empty == False):
                if (event_info['MAX'] == True):
                    idx = df_event_sb_cur['Results_float'].idxmax()
                else:
                    idx = df_event_sb_cur['Results_float'].idxmin()
                    
                wind_str = '{:+.1f}'.format(df_event_sb_cur['WindReading'][idx])
                sb_cur = common.results_to_str(df_event_sb_cur['Results_float'][idx], event_info['UNIT'], True, event_info['DISTANCE']) + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
            print('Error')
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

                sb_last = common.results_to_str(df_event_nowind_sb_last['Results_float'][idx], event_info['UNIT'], True, event_info['DISTANCE'])

            # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_last.empty == False):
                if (event_info['MAX'] == True):
                    idx = df_event_sb_last['Results_float'].idxmax()
                else:
                    idx = df_event_sb_last['Results_float'].idxmin()

                wind_str = '{:+.1f}'.format(df_event_sb_last['WindReading'][idx])
                sb_last = common.results_to_str(df_event_sb_last['Results_float'][idx], event_info['UNIT'], True, event_info['DISTANCE']) + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
            print('Error')
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

    #print(list_pb)

    return list_pb


# Skilar til baka Pandas data frame með öllum upplýsingum um ákveðna grein fyrir einhvern keppanda.
def Get_Competitor_Event_DataFrame(CompetitorCode, Event_id, EventInfo):

    # Náum í gögn úr Þór
    q = AthlAfrek.objects.filter(keppandanúmer__iexact=CompetitorCode, tákn_greinar__iexact=EventInfo['THORID_1']).order_by('dagsetning').values('árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                 'grein', 'tákn_greinar', 'vantar_vind')

    # Búum til Pandas dataframe
    df = pd.DataFrame.from_records(q)

    #df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Búum til tóma dálka
    df['árangur_float'] = 0.0
    df['árangur_str'] = ''
    df['vindur_str'] = ''

    def process_row(row):
        # Breytum öllum árangri yfir í rauntölur
        results_float = common.results_to_float(row['árangur'])
        df.at[row.name, 'árangur_float'] = results_float

        # Breytum vind yfir í string með + eða -
        if (row['vantar_vind'] == True):
            wind_str = 'N/A'
        else:
            wind_str = common.wind_to_str(row['vindur'])
        df.at[row.name, 'vindur_str'] = wind_str

        # Breytum árangri yfir í string
        if (row['rafmagnstímataka'] == 0 and EventInfo['Minimize'] == True):
            result_str = '{:.1f}'.format(results_float)
        else:
            if (EventInfo['Units'] == 5):
                result_str = '{:.0f}'.format(results_float)
            else:
                result_str = '{:.2f}'.format(results_float)

        df.at[row.name, 'árangur_str'] = result_str

    df.apply(process_row, axis=1)

    #print(df['árangur_float'])
    return df

def Get_Competitor_Event(CompetitorCode, EventID):
    df = Get_Competitor_Achievements(CompetitorCode)
    event_info = events.Get_Event_Info_by_ID_New(EventID)

    # Sía út þá grein sem beðið er um
    df_event = df[df['EventName'] == event_info['NAME_THOR']]

    # Finna besta árangur eftir ári. Löglegur og ólöglegur.
    year_arr_all, results_year_max_all, results_year_min_all, _, _, tooltip_str_max, tooltip_str_min = filter_year_best(df_event, True, False, event_info['UNIT_SYMBOL'])
    df_legal = df_event.loc[df['WindReading'] <= 2.0]
    year_arr_legal, results_year_max_legal, results_year_min_legal, _, _, tooltip_str_legal_max, tooltip_str_legal_min = filter_year_best(df_legal, True, False, event_info['UNIT_SYMBOL'])

    event_min_max_all = {'Years': year_arr_all,
                         'Max': results_year_max_all,
                         'Min': results_year_min_all,
                         'Tooltip_max': tooltip_str_max,
                         'Tooltip_min': tooltip_str_min
                        }

    event_min_max_legal = {'Years': year_arr_legal,
                           'Max': results_year_max_legal,
                           'Min': results_year_min_legal,
                           'Tooltip_max': tooltip_str_legal_max,
                           'Tooltip_min': tooltip_str_legal_min,
                          }

    #print(event_min_max_legal)
    #print('')

    pb_dates, pb, pb_tooltip = filter_progression(df_event, event_info['MAX'], event_info['UNIT_SYMBOL'])

    event_progression = {'Dates': pb_dates,
                         'PBs': pb,
                         'Tooltip': pb_tooltip
                        }

    # Make a new coulumn that is true if the the row Rafmagnstímataka is equal to 1 (True)
    df_event['Rafmagnstímataka_bool'] = df_event['Rafmagnstímataka'] == 1

    event_data = [{'Results': common.results_to_str(row['Results_float'], event_info['UNIT'], row['Rafmagnstímataka_bool'], event_info['DISTANCE']),
                   'Results_float': row['Results_float'] + common.Get_Hand_buffer(event_info['DISTANCE']) if not row['Rafmagnstímataka_bool'] else row['Results_float'],
                   'Wind': '{:+.1f}'.format(row['WindReading']),
                   'Club': row['Club'],
                   'OutIn': 0 if row['OutdoorsOrIndoors'] == 'Úti' else 1,
                   'competition_name': row['CompetitionName'],
                   'competition_id': row['CompetitionCode'],
                   'Age': row['Age'],
                   'Date': row['AchievementDate'],
                   } for _, row in df_event.iterrows()]

    return event_info, event_data, event_min_max_all, event_min_max_legal, event_progression

    #-------------------------------------------------------------------------------
def filter_year_best(df_event_data, event_max, event_time_axis, event_unit):
    year_max = df_event_data['AchievementDate'].max().year
    year_min = df_event_data['AchievementDate'].min().year

    results_year_max = []
    results_year_min = []
    results_avg = []
    results_std = []
    year_arr = []
    #org_str = []
    more_str_max = []
    more_str_min = []
    #avg_str = []

    if (df_event_data.empty == True):
        return year_arr, results_year_max, results_year_min, results_avg, results_std, more_str_max, more_str_min

    for i in range(year_min, year_max+1):
        df_event_year = df_event_data.loc[df_event_data['AchievementDate'].dt.year == i]
        if (df_event_year.empty == False):
            mean_f = df_event_year['Results_float'].mean()
            std_f = df_event_year['Results_float'].std()

            if (event_time_axis == False):
                results_avg.append( mean_f )
                results_std.append( std_f )
                #avg_str.append( '{.2f} ± {.2f}'.format(mean_f, std_f) + ' ' + event_unit )
                #results_std.append( df_event_year['Árangur_float'].std() / np.sqrt(df_event_year['Árangur_float'].count()) ) # Standard error
            else:
                results_avg.append( common.float_to_datetime(mean_f) )
                results_std.append( std_f )
                #avg_str.append( float_to_datetime(mean_f) + event_unit + ' ± {.2f} s'.format(std_f) )
                #results_std.append( df_event_year['Árangur_float'].std() / np.sqrt(df_event_year['Árangur_float'].count()) ) # Standard error

            if (event_max == True):
                idx_best = df_event_year['Results_float'].idxmax()
                idx_worst = df_event_year['Results_float'].idxmin()
                #org_str.append(df_event_year['Árangur'][idx_best])
                results_year_max.append(df_event_year['Results_float'][idx_best])
                results_year_min.append(df_event_year['Results_float'][idx_worst])
            else:
                idx_best = df_event_year['Results_float'].idxmin()
                idx_worst = df_event_year['Result_float'].idxmax()
                #org_str.append(df_event_year['Árangur'][idx_best])

                if (event_time_axis == True):
                    results_year_max.append(df_event_year['Árangur_dt'][idx_best])
                    results_year_min.append(df_event_year['Árangur_dt'][idx_worst])
                else:
                    results_year_max.append(df_event_year['Results_float'][idx_best])
                    results_year_min.append(df_event_year['Results_float'][idx_worst])

            wind_str = '{:+.1f}'.format(df_event_year['WindReading'][idx_best])
            more_str_max.append(df_event_year['Results'][idx_best] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + df_event_year['CompetitionName'][idx_best] + '<br>' + df_event_year['AchievementDate'][idx_best].strftime("%d-%m-%Y"))
            more_str_min.append(df_event_year['Results'][idx_worst] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + df_event_year['CompetitionName'][idx_worst] + '<br>' + df_event_year['AchievementDate'][idx_worst].strftime("%d-%m-%Y"))
        else:
            # Við fáum villu ef við reynum að taka min/max og enginn árangur er til fyrir árið
            results_year_max.append(None)
            results_year_min.append(None)
            results_std.append(None)
            results_avg.append(None)
            #org_str.append('')
            more_str_max.append('')
            more_str_min.append('')

        year_arr.append(i)

    return year_arr, results_year_max, results_year_min, results_avg, results_std, more_str_max, more_str_min

def filter_progression(df_event, event_max, event_unit):
    # Tökum út vind árangur
    df_event_nowind = df_event.loc[df_event['WindReading'] <= 2.0]

    # Röðum eftir dags. og árangri
    df_sorted = df_event_nowind.sort_values(by=['AchievementDate', 'Results_float'], ascending=[True, True], inplace=False)
    df_sorted.reset_index(drop=True, inplace=True)

    # Athugum hvort það sé til löglegur árangur.
    # Ef ekki notum þá vind árangur.
    if (df_sorted.empty == True):
        df_sorted = df_event.sort_values(by=['AchievementDate', 'Results_float'], ascending=[True, True], inplace=False)

    # Finnum fyrsta afrekið
    try:
        last_row = df_sorted.iloc[0]
    except:
        pb_dates = []
        pb = []
        text_place = []
        return pb_dates, pb, text_place

    pb = [last_row['Results_float']]
    pb_dates = [last_row['AchievementDate']]
    wind_str = '{:+.1f}'.format(last_row['WindReading'])
    text_place = [last_row['Results'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + last_row['CompetitionName'] + '<br>' + last_row['AchievementDate'].strftime("%d-%m-%Y")]

    for idx, row in df_sorted.iterrows():
        if (event_max == True):
            if ( (row['Results_float'] >= last_row['Results_float']) and (row['AchievementDate'] > last_row['AchievementDate']) ):
                last_row = row
                pb.append(row['Results_float'])
                pb_dates.append(row['AchievementDate'])
                wind_str = '{:+.1f}'.format(row['WindReading'])
                text_place.append(row['Results'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + row['CompetitionName'] + '<br>' + row['AchievementDate'].strftime("%d-%m-%Y"))
        else:
            if ( (row['Results_float'] <= last_row['Results_float']) and (row['AchievementDate'] > last_row['AchievementDate']) ):
                last_row = row
                pb.append(row['Results_float'])
                pb_dates.append(row['AchievementDate'])
                wind_str = '{:+.1f}'.format(row['WindReading'])
                text_place.append(row['Results'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + row['CompetitionName'] + '<br>' + row['AchievementDate'].strftime("%d-%m-%Y"))

    return pb_dates, pb, text_place

def Get_Club_By_Year(df_comp):
    year_max = df_comp['AchievementDate'].max().year
    year_min = df_comp['AchievementDate'].min().year

    club_list = {}

    for i in range(year_min, year_max+1):
        df_year = df_comp.loc[df_comp['AchievementDate'].dt.year == i]
        try:
            club = df_year.mode().iloc[0]['Club']
            club_list[i] = club
            last_club = club
        except:
            club_list[i] = last_club
            pass

    club_registry = []

    # Fyrsta félagið
    cur_date = df_comp['AchievementDate'].min().to_pydatetime() # Pandas returns timestamp not datetime
    cur_club = club_list[year_min]

    for year in club_list:
        next_club = club_list[year]
        if (next_club != cur_club):
            next_date = datetime(year, 1, 1)
            club_registry.append({'from': cur_date, 'to': next_date-timedelta(days=1), 'club': cur_club})
            cur_club = next_club
            cur_date = next_date

    if (year == year_max):
        next_date = None
        club_registry.append({'from': cur_date, 'to': next_date, 'club': next_club})

    return club_list, club_registry