from django.db.models import Q

from .models import Stanok, Instrument, Rigging


def get_stanok_list_by_search_query(search_query):
    return Stanok.objects.filter(Q(name__icontains=search_query) |
                                 Q(description__icontains=search_query))


def get_instrument_list_by_search_query(search_query):
    return Instrument.objects.filter(Q(name__icontains=search_query) |
                                     Q(description__icontains=search_query))


def get_rigging_list_by_search_query(search_query):
    return Rigging.objects.filter(Q(name__icontains=search_query) |
                                  Q(description__icontains=search_query))
