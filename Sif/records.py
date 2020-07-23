from django.http import Http404

# Database
# We only use AthlCompetitors for information about competitors
# and AthlAfrek for the achievements.
from Sif.models import AthlCompetitors, AthlAfrek, Competitors, AthlMetaskrFr
from django.db.models import Q

# Settings
from Sif import settings

def Get_Competitor_Records(CompetitorCode):
    q = AthlMetaskrFr.objects.all().filter(methafi__iexact=CompetitorCode).order_by('aldursflokkur_frí', 'dagsetning_mets')

    record_list = []
    for record in q:
        wind_str = '{:+.1f}'.format(float(record.vindur))
        results = results_to_float(record.árangur.replace(',', '.'))
        results_str = record.árangur
        date_str = format_date(record.dagsetning_mets.date(), "d MMM yyyy", locale='is_IS').upper()
        active = record.virkt
        age = record.aldur_methafa
        agegroup = record.aldursflokkur_frí
        inout = record.úti_inni
        club = record.félag_methafa
        event = record.grein

        record_info = {'Event': event,
                       'Club': club,
                       'Inout': inout,
                       'AgeGroup': agegroup,
                       'age': age,
                       'isActive': active,
                       'Date': date_str,
                       'Results': results,
                       'Results_str': results_str,
                       'Wind': wind_str
                      }

        record_list.append(record_info)

    return record_list