from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from info_helper import format_duration, get_duration, is_visit_long
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visit = Visit.objects.filter(passcard=passcard)
    this_card_visit = []
    for visit in passcard_visit:
        entered_at = localtime(visit.entered_at)
        duration = get_duration(visit)
        visit_time = format_duration(duration)
        visit_flag = is_visit_long(duration)
        this_card_visit.append(
            {
                'entered_at': entered_at,
                'duration': visit_time,
                'is_strange': visit_flag
            }, )
    context = {'passcard': passcard, 'this_passcard_visits': this_card_visit}
    return render(request, 'passcard_info.html', context)
