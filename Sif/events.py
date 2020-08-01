from django.http import Http404

import os
import pandas as pd

from Sif import settings
from Sif import common

# Events
EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')
df_event_list = pd.read_pickle(EVENT_LIST_FILENAME)

def Get_Event_Info(Event_id):
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

        EventShorterName = df_event_list['Name_ISL'].values[Event_id].replace('metra', 'm').replace('hlaup', '').replace('grind', 'gr.').replace('atrennu', 'atr.')
        Event_Info = {'THORID_1': df_event_list['THORID_1'].values[Event_id],
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