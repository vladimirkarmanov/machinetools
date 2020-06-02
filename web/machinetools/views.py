from django.views.generic import DetailView, TemplateView, ListView

from .mixins import ListViewMixin
from .models import Stanok, Instrument, Rigging, Manual
from .services import (
    get_stanok_list_by_search_query,
    get_instrument_list_by_search_query,
    get_rigging_list_by_search_query,
    get_manual_list_by_search_query
)


class IndexView(TemplateView):
    template_name = 'machinetools/index.html'


class StanokListView(ListViewMixin, ListView):
    model = Stanok
    template_name = 'machinetools/stanok_list.html'
    default_order = 'group'
    orders = ['power', 'rotation_frequency']

    def get_queryset_by_search_query(self, search_query):
        return get_stanok_list_by_search_query(search_query)


class InstrumentListView(ListViewMixin, ListView):
    model = Instrument
    template_name = 'machinetools/instrument_list.html'
    default_order = 'name'
    orders = ['workpiece_type', 'application_area']

    def get_queryset_by_search_query(self, search_query):
        return get_instrument_list_by_search_query(search_query)


class RiggingListView(ListViewMixin, ListView):
    model = Rigging
    template_name = 'machinetools/rigging_list.html'
    default_order = 'name'
    orders = ['rigging_type']

    def get_queryset_by_search_query(self, search_query):
        return get_rigging_list_by_search_query(search_query)


class ManualListView(ListViewMixin, ListView):
    model = Manual
    template_name = 'machinetools/manual_list.html'
    default_order = 'name'
    orders = []

    def get_queryset_by_search_query(self, search_query):
        return get_manual_list_by_search_query(search_query)


class StanokDetailView(DetailView):
    model = Stanok
    template_name = 'machinetools/stanok_detail.html'


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = 'machinetools/instrument_detail.html'


class RiggingDetailView(DetailView):
    model = Rigging
    template_name = 'machinetools/rigging_detail.html'
