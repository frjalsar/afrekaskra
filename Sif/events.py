from django.http import Http404

import os
import pandas as pd
import re

from Sif import settings
from Sif import common

from Sif.event_var import event_list, event_dict

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

#def Get_Event_Info_by_ID():
#    return None

def Find_Distance(event_name_isl_str):
    distance = -1.0
    reg = re.findall(r'(\d+) metra', event_name_isl_str)
    if (len(reg) > 0):
        distance = int(reg[0])
    else:
        reg = re.findall(r'(\d+\.\d+) km', event_name_isl_str.replace(',', '.'))
        if (len(reg) > 0):
            distance = (float(reg[0])*1000)
        else:
            if (re.search('maraþon', event_name_isl_str, re.IGNORECASE)):
                if (re.search('hálft', event_name_isl_str, re.IGNORECASE)):
                    distance = 21097.5
                else:
                    distance = 42195
            else:
                distance = -1.0
    return distance

def Get_Event_Info_by_Name(EventName):
    NameofEvent = EventName.replace(',', '.').replace('(f)', '(flögutímar)')
    try:
        event_info = event_dict[NameofEvent]
        event_info['NAME_THOR'] = NameofEvent
        event_info['EVENT_ID'] = event_list.index(NameofEvent)
        event_info['DISTANCE'] = Find_Distance(NameofEvent)
    except:
        print('VILLA: Fann ekki grein {}'.format(NameofEvent))
        print(NameofEvent)
        event_info = event_dict['Óþekkt grein']
        event_info['NAME_SHORT'] = NameofEvent
        event_info['EVENT_ID'] = 1
        event_info['DISTANCE'] = -1
    
    return event_info

def Get_Event_Info_by_ID_New(EventID):
    EventName = event_list[EventID]
    event_info = Get_Event_Info_by_Name(EventName)
    return event_info

def Get_Event_Info_by_ThordID(ThorID_2, ThorID_1, AgeGroup=''):
    #print('Get_Event_Info Start')
    #print(AgeGroup)
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
                print('Get_Event_Info_by_ThordID: VARÚÐ leit skilaði fleiri en einni grein!!')
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
    
    #print('Get Event info end')
    #print('')
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

            # Þetta er líklega hlaupa grein
            # Reynum að finna vegalengdina á henni
            distance = Find_Distance(df_event_list['Name_ISL'].values[Event_id])
            
        else:
            minimize = False
            distance = -1.0 # -1 í vegalengd ef greinin er ekki hlaupa grein

        EventShorterName = df_event_list['Name_ISL'].values[Event_id].replace('metra', 'm').replace('boðhlaup', 'bh.').replace(' hlaup', ' ').replace('grind', 'gr.').replace('atrennu', 'atr.')
        Event_Info = {'THORID_1': df_event_list['THORID_1'].values[Event_id],
                      'THORID_2': df_event_list['THORID_2'].values[Event_id],
                      'Event_ID': Event_id,
                      'AgeGroup': df_event_list['AgeGroup'].values[Event_id],
                      'Units': Units,
                      'Units_symbol': common.Units_symbol[Units],
                      'Minimize': minimize,
                      'ShortName': EventShorterName.strip(), #df_event_list['ShortName'].values[Event_id],
                      'Name_ISL': df_event_list['Name_ISL'].values[Event_id],
                      'HasWind': df_event_list['Wind'].values[Event_id],
                      'Distance': distance}
    except:
        print(Event_id)
        raise Http404('Gat ekki fundið grein.')

    return Event_Info