from datetime import timezone, datetime
from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    print(entered_at.second)
    if visit.leaved_at == None:
        date_none = localtime(datetime.now(timezone.utc))
        delta = date_none - entered_at
    else:
        leaved_time = localtime(visit.leaved_at)
        delta = leaved_time - entered_at
    return delta


def format_duration(delta):
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes}"


def is_visit_long(delta, minutes=60):
    seconds = minutes * minutes
    long_visit = delta.seconds > seconds
    return long_visit