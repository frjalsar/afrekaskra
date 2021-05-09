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

def Get_Competitor_Events_Info(CompetitorCode=None):
    #print('Event_info for {:d}'.format(CompetitorCode))
    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode)
    df = pd.DataFrame.from_records(q.values_list('lína', 'nafn', 'keppandanúmer',
                                                 'árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                 'grein', 'tákn_greinar', 'vantar_vind', 'flokkur'),
                                                 columns=['lína', 'nafn', 'keppandanúmer',
                                                          'Árangur', 'Vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                          'grein', 'tákn_greinar', 'vantar_vind', 'flokkur'])

    # úti_inni: Úti = 0, Inni = 1
    df['Dagsetn.'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['Árangur_float'] = df['Árangur'].map(common.results_to_float)

    def Map_func(x):
        #print(x)
        return events.Get_Event_Info_by_ThordID(x['grein'], x['tákn_greinar'], x['flokkur'])

    # Búa til lista yfir greinar
    list_events = df[['grein', 'tákn_greinar', 'flokkur']].copy() # copy til að búa til afrit
    list_events['Event_id'] = list_events.apply(Map_func, axis=1)
    list_events.drop_duplicates(subset=['Event_id'], inplace=True) # Henda út endurtekningum
    list_events.reset_index(drop=True, inplace=True) # Endur númera index

    #print('list_events')
    #print(list_events)
    #print('')

    list_pb = []
    list_sb = []
    for index, row in list_events.iterrows():
        #print(i)
        #try:
        #    event_id = events.df_event_list[events.df_event_list['THORID_1'] == i].index.tolist()[0]
        #except:
        #    print('ERROR gat ekki fundið grein')
        #    print(i)
        #    print(type(i))
        #    pass
        ##print(event_id)
        #event_info = events.Get_Event_Info_by_ID(event_id)
        ##print(event_info)
        try:
            event_info = events.Get_Event_Info_by_ThordID(row['grein'], row['tákn_greinar'], row['flokkur'])
        except:
            continue

        # Flokka út Grein
        df_event = df.loc[(df['grein'] == row['grein']) & (df['flokkur'] == row['flokkur'])].copy() # Búum til copy til að breyta
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
        pb_out_date = datetime.datetime(1970, 1, 1)

        pb_in = ''
        pb_in_date = datetime.datetime(1970, 1, 1)

        #try:
            # Finnum PB inni ef það er til
        if (df_event_in.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_in['Árangur_float'].idxmax()
            else:
                idx = df_event_in['Árangur_float'].idxmin()

            pb_in = df_event_in['Árangur'][idx]
            pb_in_date = df_event_in['dagsetning'][idx]

        # Finnum PB úti með löglegum árangri ef það er til
        if (df_event_nowind_out.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_nowind_out['Árangur_float'].idxmax()
            else:
                idx = df_event_nowind_out['Árangur_float'].idxmin()

            pb_out = df_event_nowind_out['Árangur'][idx]
            pb_out_date = df_event_nowind_out['dagsetning'][idx]

        # Ef ekki þá athugum við ólöglegan árangur
        elif (df_event_out.empty == False):
            if (event_info['Minimize'] == False):
                idx = df_event_out['Árangur_float'].idxmax()
            else:
                idx = df_event_out['Árangur_float'].idxmin()

            pb_out = df_event_out['Árangur'][idx] + ' ({:+.1f}'.format(df_event_out['Vindur'][idx]) + ' m/s)'
            pb_out_date = df_event_out['dagsetning'][idx]
        #except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
        #    pass

        date_now = datetime.date.today()
        date_from_cur = np.datetime64(datetime.datetime(date_now.year, 1, 1, 0, 0, 0)) # 1 jan þessi ári
        date_to_cur = np.datetime64(date_now) # Í dag

        date_from_last = np.datetime64(datetime.datetime(date_now.year-1, 1, 1, 0, 0, 0)) # 1 jan á seinasta ári
        date_to_last = np.datetime64(datetime.datetime(date_now.year-1, 12, 31, 0, 0, 0)) # 31 des á seinasta ári

        # Árangur með löglegum vindi
        mask = df_event['Vindur'] <= 2.0
        df_event_nowind = df_event.loc[mask]

        #print(type(date_now))
        #print(df_event.dtypes)

        # Þetta ár
        #mask_cur = np.logical_and(df_event['dagsetning'] < date_to_cur, date_from_cur < df_event['dagsetning'])
        df_event_sb_cur = df_event.loc[df_event['Dagsetn.'].dt.year == 2020]
        #print(df_event_sb_cur)
        #if (df_event_sb_cur.empty == False):
        #    print(df_event_sb_cur)

        # Þetta ár löglegur vindur
        #mask_cur_nowind = np.logical_and(df_event_nowind['dagsetning'] < date_to_cur, date_from_cur < df_event_nowind['dagsetning'])
        df_event_nowind_sb_cur = df_event_nowind.loc[df_event['Dagsetn.'].dt.year == date_now.year]

        # Fyrra
        #mask_last = np.logical_and(df_event['dagsetning'] < date_to_last, date_from_last <=df_event['dagsetning'])
        df_event_sb_last = df_event.loc[df_event['Dagsetn.'].dt.year == (date_now.year-1)]

        # Í fyrra löglegur árangur
        #mask_last_nowind = np.logical_and(df_event_nowind['dagsetning'] < date_to_last, date_from_last < df_event_nowind['dagsetning'])
        df_event_nowind_sb_last = df_event_nowind.loc[df_event['Dagsetn.'].dt.year == (date_now.year-1)]

        sb_cur = ''
        try:
            # Finnum SB inni ef það er til
            if (df_event_nowind_sb_cur.empty == False):
                #print(df_event_nowind_sb_cur)
                if (event_info['Minimize'] == False):
                    idx = df_event_nowind_sb_cur['Árangur_float'].idxmax()
                else:
                    idx = df_event_nowind_sb_cur['Árangur_float'].idxmin()
                    
                sb_cur = df_event_nowind_sb_cur['Árangur'][idx]
                #print(sb_cur)

                # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_cur.empty == False):
                if (event_info['Minimize'] == False):
                    idx = df_event_sb_cur['Árangur_float'].idxmax()
                else:
                    idx = df_event_sb_cur['Árangur_float'].idxmin()
                    
                wind_str = '{:+.1f}'.format(df_event_sb_cur['Vindur'][idx])
                sb_cur = df_event_sb_cur['Árangur'][idx] + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
        #    sub_cur = ''
            pass

        sb_last = ''
        try:
            # Finnum SB úti með löglegum árangri ef það er til
            if (df_event_nowind_sb_last.empty == False):
                if (event_info['Minimize'] == False):
                    idx = df_event_nowind_sb_last['Árangur_float'].idxmax()
                else:
                    idx = df_event_nowind_sb_last['Árangur_float'].idxmin()

                sb_last = df_event_nowind_sb_last['Árangur'][idx]

            # Ef ekki þá athugum við ólöglegan árangur
            elif (df_event_sb_last.empty == False):
                if (event_info['Minimize'] == False):
                    idx = df_event_sb_last['Árangur_float'].idxmax()
                else:
                    idx = df_event_sb_last['Árangur_float'].idxmin()

                wind_str = '{:+.1f}'.format(df_event_sb_last['Vindur'][idx])
                sb_last = df_event_sb_last['Árangur'][idx] + ' (' + wind_str + ' m/s)'
        except:
            # Ef eitthvað klikkar þá sleppum við þessari grein
            #print('Error')
            #sb_last = ''
            pass



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

        #sb_out = ''
        #sb_in = ''

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

        #print(sb_cur)

        # if (pb_out == ''):
        #     pb_out_date_str = ''
        # else:
        #     pb_out_date_str = str(pb_out_date.year)

        # if (pb_in == ''):
        #     pb_in_date_str = ''
        # else:
        #     pb_in_date_str = str(pb_in_date.year)

        # Bæta við í listan
        list_pb.append({'EventName': event_info['Name_ISL'],
                        'EventShortName': event_info['ShortName'],
                        'EventUnit': event_info['Units_symbol'],
                        'EventID': event_info['Event_ID'],
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

def Get_Competitor_Event(CompetitorCode, Event_id):
    event_info = events.Get_Event_Info_by_ID(Event_id)

    flokkur = event_info['AgeGroup']
    if (flokkur == '-1'):
        flokkur = ''
    
    q = AthlAfrek.objects.all().filter(keppandanúmer__iexact=CompetitorCode, grein__iexact=event_info['THORID_2'], flokkur__iexact=flokkur).order_by('dagsetning')
    
    df = pd.DataFrame.from_records(q.values_list('árangur', 'vindur', 'félag',
                                                 'aldur_keppanda', 'heiti_móts', 'mót',
                                                 'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                 'grein', 'tákn_greinar', 'vantar_vind',
                                                 'flokkur'),
                                                 columns=['árangur', 'vindur', 'félag',
                                                          'aldur_keppanda', 'heiti_móts', 'mót',
                                                          'dagsetning', 'rafmagnstímataka', 'úti_inni',
                                                          'grein', 'tákn_greinar', 'vantar_vind',
                                                          'flokkur'])

    # úti_inni: Úti = 0, Inni = 1
    df['dagsetning'] = pd.to_datetime(df['dagsetning'], dayfirst=True)

    # Breytum öllum árangri yfir í rauntölur
    df['árangur_float'] = df['árangur'].map(common.results_to_float)

    year_arr_all, results_year_max_all, results_year_min_all, _, _, tooltip_str_max, tooltip_str_min = filter_year_best(df, True, False, event_info['Units_symbol'])
    df_legal = df.loc[df['vindur'] <= 2.0]
    year_arr_legal, results_year_max_legal, results_year_min_legal, _, _, tooltip_str_legal_max, tooltip_str_legal_min = filter_year_best(df_legal, True, False, event_info['Units_symbol'])

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

    pb_dates, pb, pb_tooltip = filter_progression(df, not event_info['Minimize'], event_info['Units_symbol'])

    event_progression = {'Dates': pb_dates,
                         'PBs': pb,
                         'Tooltip': pb_tooltip
                        }

    event_data = []
    for index, row in df.iterrows():
        if (row.vantar_vind == True):
            wind_str = 'N/A'
        else:
            wind_str = '{:+.1f}'.format(row.vindur)

        if (row.rafmagnstímataka == 0 and event_info['Minimize'] == True):
            result_str = '{:.1f}'.format(row.árangur_float)
        else:
            if (event_info['Units'] == 5):
                result_str = '{:.0f}'.format(row.árangur_float)
            else:
                result_str = '{:.2f}'.format(row.árangur_float)

        event_data.append({'Results': result_str,
                           'Wind': wind_str,
                           'Club': row['félag'],
                           'OutIn': row['úti_inni'],
                           'competition_name': row['heiti_móts'],
                           'competition_id': row['mót'],
                           'Age': row['aldur_keppanda'],
                           'Date': row['dagsetning'], #format_date(row['dagsetning'], "d MMM yyyy",locale='is_IS').upper(),
                           'ElectricTiming': row['rafmagnstímataka'],
                           'MissingWind': row['vantar_vind']
                           })

    return event_info, event_data, event_min_max_all, event_min_max_legal, event_progression

def Get_List_of_Events(CompetitorCode=None, Event_id=None):
    return None
    if (CompetitorCode == None):
        q = AthlAfrek.objects.order_by('tákn_greinar').values_list('grein', flat=True).distinct()
    else:
        q = AthlAfrek.objects.values_list('grein', flat=True).distinct().filter(keppandanúmer__iexact=CompetitorCode)

    Event_list = []
    for event in q:
        try:
            event_info = {'EVENT_ID': int(events.df_event_list[events.df_event_list['THORID_1'] == event].index[0]),
                        'Name_ISL': events.df_event_list[events.df_event_list['THORID_1'] == event]['Name_ISL'].values[0],
                        'Name_ENG': events.df_event_list[events.df_event_list['THORID_1'] == event]['Name_ENG'].values[0],
                        'Name_short': events.df_event_list[events.df_event_list['THORID_1'] == event]['ShortName'].values[0],
                        'Units': int(events.df_event_list[events.df_event_list['THORID_1'] == event]['Units'].values[0]),
                        'Wind': bool(events.df_event_list[events.df_event_list['THORID_1'] == event]['Wind'].values[0])}
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

def Top_100_List(Event_id, Year, IndoorOutDoor, Gender, AgeStart, AgeEnd, Legal, ISL, BestByAth, N=100):
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
        q = AthlAfrek.objects.all().filter(grein__iexact=Event_Info['THORID_2'], tákn_greinar__iexact=Event_Info['THORID_1'])
        print(Event_Info)

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

    return Achievements_list[:N], Event_Info

def Top_List():
    Top_Women = []
    Top_Men = []

    Women_Events = [82, 86, 6, 7, 27, 48, 52, 97, 19, 30, 62, # Hlaup
                    179, 252, 143, 239, # Stökk
                    227, 168, 216, 164, # Köst
                    1001, 1011 # Þraut
                    ] 
    Men_Events   = [82, 83, 6, 15, 27, 48, 49, 97, 19, 30, 62, # Hlaup
                    179, 252, 143, 239, # Stökk
                    226, 162, 212, 152, # Köst
                    1011, 1021 # Þraut
                    ]

    #current_year = datetime.datetime.now().year
    current_year = 2020

    # -- Women
    for event_id in Women_Events:
        Top_W, Event_info_W = Top_100_List(event_id, current_year, 2, 2, 0, 99, True, 0, True, 1)

        try:
            Top_Women.append({'Name'          : Top_W[0]['name'],
                              'CompetitorID'  : Top_W[0]['competitor_code'],
                              'Results'       : common.results_to_str(float(Top_W[0]['results']), Event_info_W['Units'], True),
                              'OutInn'        : Top_W[0]['outdoor_indoor'],
                              'Club'          : Top_W[0]['club'],
                              'EventName'     : Event_info_W['ShortName'],
                              'EventID'       : event_id,
                              'Units_symbol'  : Event_info_W['Units_symbol']
                              })
        except IndexError: # Index error þýðir líklegast að engin árangur fannst
            pass

    # -- Men
    for event_id in Men_Events:
        Top_M, Event_info_M = Top_100_List(event_id, current_year, 2, 1, 0, 99, True, 0, True, 1)

        try:

            Top_Men.append({'Name'          : Top_M[0]['name'],
                            'CompetitorID'  : Top_M[0]['competitor_code'],
                            'Results'       : common.results_to_str(float(Top_M[0]['results']), Event_info_M['Units'], True),
                            'OutInn'        : Top_M[0]['outdoor_indoor'],
                            'Club'          : Top_M[0]['club'],
                            'EventName'     : Event_info_M['ShortName'],
                            'EventID'       : event_id,
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


#-------------------------------------------------------------------------------
def filter_year_best(df_event_data, event_max, event_time_axis, event_unit):
    year_max = df_event_data['dagsetning'].max().year
    year_min = df_event_data['dagsetning'].min().year

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
        return year_arr, results_year_max, results_year_min, results_avg, results_std

    for i in range(year_min, year_max+1):
        df_event_year = df_event_data.loc[df_event_data['dagsetning'].dt.year == i]
        if (df_event_year.empty == False):
            mean_f = df_event_year['árangur_float'].mean()
            std_f = df_event_year['árangur_float'].std()

            if (event_time_axis == False):
                results_avg.append( mean_f )
                results_std.append( std_f )
                #avg_str.append( '{.2f} ± {.2f}'.format(mean_f, std_f) + ' ' + event_unit )
                #results_std.append( df_event_year['Árangur_float'].std() / np.sqrt(df_event_year['Árangur_float'].count()) ) # Standard error
            else:
                results_avg.append( float_to_datetime(mean_f) )
                results_std.append( std_f )
                #avg_str.append( float_to_datetime(mean_f) + event_unit + ' ± {.2f} s'.format(std_f) )
                #results_std.append( df_event_year['Árangur_float'].std() / np.sqrt(df_event_year['Árangur_float'].count()) ) # Standard error

            if (event_max == True):
                idx_best = df_event_year['árangur_float'].idxmax()
                idx_worst = df_event_year['árangur_float'].idxmin()
                #org_str.append(df_event_year['Árangur'][idx_best])
                results_year_max.append(df_event_year['árangur_float'][idx_best])
                results_year_min.append(df_event_year['árangur_float'][idx_worst])
            else:
                idx_best = df_event_year['árangur_float'].idxmin()
                idx_worst = df_event_year['árangur_float'].idxmax()
                #org_str.append(df_event_year['Árangur'][idx_best])

                if (event_time_axis == True):
                    results_year_max.append(df_event_year['Árangur_dt'][idx_best])
                    results_year_min.append(df_event_year['Árangur_dt'][idx_worst])
                else:
                    results_year_max.append(df_event_year['árangur_float'][idx_best])
                    results_year_min.append(df_event_year['árangur_float'][idx_worst])

            wind_str = '{:+.1f}'.format(df_event_year['vindur'][idx_best])
            more_str_max.append(df_event_year['árangur'][idx_best] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + df_event_year['heiti_móts'][idx_best] + '<br>' + df_event_year['dagsetning'][idx_best].strftime("%d-%m-%Y"))
            more_str_min.append(df_event_year['árangur'][idx_worst] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + df_event_year['heiti_móts'][idx_worst] + '<br>' + df_event_year['dagsetning'][idx_worst].strftime("%d-%m-%Y"))
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
    df_event_nowind = df_event.loc[df_event['vindur'] <= 2.0]

    # Röðum eftir dags. og árangri
    df_sorted = df_event_nowind.sort_values(by=['dagsetning', 'árangur_float'], ascending=[True, True], inplace=False)
    df_sorted.reset_index(drop=True, inplace=True)

    # Athugum hvort það sé til löglegur árangur.
    # Ef ekki notum þá vind árangur.
    if (df_sorted.empty == True):
        df_sorted = df_event.sort_values(by=['dagsetning', 'árangur_float'], ascending=[True, True], inplace=False)

    # Finnum fyrsta afrekið
    last_row = df_sorted.iloc[0]

    pb = [last_row['árangur_float']]
    pb_dates = [last_row['dagsetning']]
    wind_str = '{:+.1f}'.format(last_row['vindur'])
    text_place = [last_row['árangur'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + last_row['heiti_móts'] + '<br>' + last_row['dagsetning'].strftime("%d-%m-%Y")]

    for idx, row in df_sorted.iterrows():
        if (event_max == True):
            if ( (row['árangur_float'] >= last_row['árangur_float']) and (row['dagsetning'] > last_row['dagsetning']) ):
                last_row = row
                pb.append(row['árangur_float'])
                pb_dates.append(row['dagsetning'])
                wind_str = '{:+.1f}'.format(row['vindur'])
                text_place.append(row['árangur'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + row['heiti_móts'] + '<br>' + row['dagsetning'].strftime("%d-%m-%Y"))
        else:
            if ( (row['árangur_float'] <= last_row['árangur_float']) and (row['dagsetning'] > last_row['dagsetning']) ):
                last_row = row
                pb.append(row['árangur_float'])
                pb_dates.append(row['dagsetning'])
                wind_str = '{:+.1f}'.format(row['vindur'])
                text_place.append(row['árangur'] + ' ' + event_unit + ' (' + wind_str + ' m/s)<br>' + row['heiti_móts'] + '<br>' + row['dagsetning'].strftime("%d-%m-%Y"))

    return pb_dates, pb, text_place

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