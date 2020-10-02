from django.http import Http404

import os
import pandas as pd

from Sif import settings
from Sif import common

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

def Get_Event_Info_by_ThordID(ThorID_2, ThorID_1, AgeGroup=''):
    print('Get_Event_Info Start')
    print(AgeGroup)
    if (AgeGroup == ''):
        AgeGroup = '-1'

    Event_id_list = df_event_list[(df_event_list['THORID_2'] == ThorID_2) & (df_event_list['AgeGroup'] == AgeGroup)].index.tolist()
    print(Event_id_list)

    if (len(Event_id_list) == 0):
        Event_id_list = df_event_list[(df_event_list['THORID_2'] == ThorID_2) & (df_event_list['THORID_1'] == ThorID_1)].index.tolist()


    if (len(Event_id_list) > 1):
        Event_id_list = df_event_list[(df_event_list['THORID_2'] == ThorID_2) & (df_event_list['THORID_1'] == ThorID_1)].index.tolist()
        print(Event_id_list)
        if (len(Event_id_list) > 1):
            Event_id_list = df_event_list[(df_event_list['THORID_2'] == ThorID_2) & (df_event_list['AgeGroup'] == AgeGroup) & (df_event_list['THORID_1'] == ThorID_1)].index.tolist()
            print(Event_id_list)
            if (len(Event_id_list) > 1):
                print('Get_Event_Info_by_ThordID: VARÚÐ leit skilaði fleirri en einni grein!!')
                print(ThordID)
                print(AgeGroup)
                print(Event_id_list)

    if (len(Event_id_list) == 0):
        print('Get_Event_Info_by_ThordID: Villa fann ekki grein!')
        print(ThorID_2)
        print(ThorID_1)
        print(AgeGroup)
        raise Http404
        #return None
    
    try:
        Event_id = Event_id_list[0]
    except:
        print('')
        print(ThorID_2)
        print(ThorID_1)
        print(AgeGroup)
        print('')
    Event_Info = Get_Event_Info_by_ID(Event_id)
    
    print('Get Event info end')
    print('')
    return Event_Info

def Get_Event_Info_by_ID(Event_id):
    try:
        Units = df_event_list['Units'].values[Event_id]
        #0, # No units!
        #'metrar': 1, # Meters
         #'sek.': 2, # ss,dd
         #'mín.': 3, # mm:ss
         #'klst.': 4, # hh:mm:ss,dd
         #'stig': 5, # Points
         #'Ungl.stig': 6 # Points junior
        if (Units in [0, 2, 3, 4]):
            minimize = True
        else:
            minimize = False

        EventShorterName = df_event_list['Name_ISL'].values[Event_id].replace('metra', 'm').replace('boðhlaup', 'bh.').replace(' hlaup', ' ').replace('grind', 'gr.').replace('atrennu', 'atr.')
        Event_Info = {'THORID_1': df_event_list['THORID_1'].values[Event_id],
                      'THORID_2': df_event_list['THORID_2'].values[Event_id],
                      'Event_ID': Event_id,
                      'AgeGroup': df_event_list['AgeGroup'].values[Event_id],
                      'Units': Units,
                      'Units_symbol': common.Units_symbol[Units],
                      'Minimize': minimize,
                      'ShortName': EventShorterName, #df_event_list['ShortName'].values[Event_id],
                      'Name_ISL': df_event_list['Name_ISL'].values[Event_id],
                      'HasWind': df_event_list['Wind'].values[Event_id]}
    except:
        print(Event_id)
        raise Http404('Gat ekki fundið grein.')

    return Event_Info