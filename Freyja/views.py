from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
#from django.db.models import Q

# Other
import datetime

# Gagnagrunnur
from Freyja.models import AthlCompetitors

# Front page
def front_page(requests):
    return render(requests, 'front_page.html')

# Get_Competitor_Info
# Looks upp information about a competitor from the AthlCompetitors table.
# Inn:
#  CompetitorCode: Fiffós ID code for the competitor
# Out:
#  Competitor_Info: A dictionary containing name, year of birth and club.
def Get_Competitor_Info(CompetitorCode):
    
    # Look upp the competitor in the table. We want an exact match.
    try:
        q = AthlCompetitors.objects.get(númer__iexact=CompetitorCode)
            # Make a Competitor dict with information about the competitor
        Competitor_Info = {'CompetitorCode': CompetitorCode,
                           'Name': q.nafn,
                           'FirstName': q.nafn.split(' ')[0],
                           'LastName': q.nafn.split(' ')[-1],
                           'YOB': q.fæðingarár,
                           'Club': q.félag,
                           'Datetime': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
    except AthlCompetitors.DoesNotExist:
        raise Http404('Gat ekki fundið keppanda.')

    return Competitor_Info


def competitor(request, CompetitorCode=None, Event=None):
    Competitor_info = Get_Competitor_Info(CompetitorCode)
    return render(request, 'competitor.html', {'Competitor': Competitor_info})
