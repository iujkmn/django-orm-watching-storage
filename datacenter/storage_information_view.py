from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from info_helper import format_duration,get_duration,is_visit_long


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)
    not_closed_visits = []
    for visit in not_leaved:
        duration = get_duration(visit)
        entry_localtime = localtime(visit.entered_at)
        visit_time = format_duration(duration)
        visit_flag = is_visit_long(duration)
        person = visit.passcard 

        not_closed_visits.append(
            {
                'who_entered': person,
                'entered_at': entry_localtime,
                'duration': visit_time,
                'is_strange': visit_flag
            }
        )
    context = {
        'non_closed_visits': not_closed_visits,
    }
    return render(request, 'storage_information.html', context)
