from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView

# Front page
def front_page(requests):
    return render(requests, 'front_page.html')

#-------------------------------------------------------------------------------
# View sem skilar til baka síðu með tölfu um greinina sem er valin
def competitor(request, CompetitorCode=None, Event=None):

    # Ef ekkert CompetitorCode, byrta þá síðu til finna keppanda
    if (CompetitorCode is None):
        return render(request, 'competitor_find.html')

    try:
        CompetitorCode = int(CompetitorCode)
        #Event = int(Event)
    except ValueError:
        raise Http404('Error')

    try:
        Competitor, df = Scrape_Competitor_Data(CompetitorCode)
    except:
        return HttpResponseServerError('Tókst ekki að ná í gögn úr afrekaskrá FRÍ.')

    if (df is None and Competitor is None):
        return HttpResponseServerError('Tókst ekki að ná í gögn úr afrekaskrá FRÍ.')

    # Ef engin grein er valinn þá finnum við hvaða grein keppandinn hefur
    # oftast keppt í ( df.mode().iloc[0] ) og veljum hana ( event_list.index(...) )
    if (Event is None):
        try:
            Event = event_list.index( df.mode().iloc[0]['Keppnisgrein'] )
        except:
            Event = None

    # Flokka út greinina sem er valin
    Competitor_events, df_event = Filter_Competitor_Event(Competitor, Event, df)

    if (df_event is None):
        return HttpResponseServerError('df_event is None')

    # Breyta Panda dataframe í HTML tölfu
    # Henda út dálknum með keppnisgreininni
    event_str = Competitor['Event']
    drop_col = ['Keppnisgrein', 'Árangur_float']
    if (event_dict[event_str]['TIME_AXIS'] == True):
        drop_col.append('Árangur_dt')
        drop_col.append('Sería')

    html_table = df_event.drop(drop_col, 1).to_html(index=False,
                                                    na_rep='',
                                                    classes='table table-striped table-bordered table-data',
                                                    border='0',
                                                    formatters={'Dagsetn.': lambda x: x.strftime('%-d %b %Y')}
                                                    )

    # PB Taflan
    pb_html_table = Stats_Competitor(Competitor, df)

    # Plotta upp árs besta og tíma-raðar gröfin
    plot_div_year = year_best_graph_div(Competitor, df_event)
    plot_div_time = time_series_graph_div(Competitor, df_event)
    plot_div_pb   = progression_graph_div(Competitor, df_event, 'Árangur', 'Heiti móts')

    # Hvernig á að raða töflunni með gögnunum
    if (event_dict[event_str]['MAX'] == True):
        TBL_DATA_SORT = 'desc'
    else:
        TBL_DATA_SORT = 'asc'

    # Senda til baka gögnin
    return render(request, 'competitor.html', {'Competitor': Competitor})
