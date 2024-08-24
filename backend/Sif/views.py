from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.generic.base import RedirectView
#from django.db.models import Q

from Sif import settings
from Sif import data

# Other
import os
import re

# Events

#EVENT_LIST_FILENAME = os.path.join(settings.BASE_DIR, 'Sif/event_list.pickle')

 # Senda allt sem fer ekki á API á index.html
def view_404(request, exception=None):
    if (re.match('^/api/*', request.path) is None):
        return render(request, 'index.html')
    else:
        return render(request, '404.html', status=404)

# def Print_list_vertically(my_list):
#     for i in my_list:
#         print(i)
#     return None

# # Front page
# def front_page(requests):
#     return render(requests, 'front_page.html')


# def competitor(request, CompetitorCode=None, Event=None):
#     #print(Get_List_of_Events_for_Competitor(CompetitorCode))
#     #Print_list_vertically(Get_List_of_Events())
#     #print(Get_List_of_Events())
#     #Get_List_of_Events()
#     # if (CompetitorCode == None):
#     #     return redirect('front_page')
#     # else:
#     #     Competitor_info = data.Get_Competitor_Info(CompetitorCode)
#     return render(request, 'competitor.html')

# def top_lists(request):
#     #years = data.Get_List_of_Years()
    
#     return render(request, 'top_lists.html')
