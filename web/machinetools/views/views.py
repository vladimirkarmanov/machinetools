from django.views.generic import DetailView, TemplateView, ListView

from machinetools.models import Stanok, Instrument, Rigging, Manual
from machinetools.services import (
    get_stanok_list_by_search_query,
    get_instrument_list_by_search_query,
    get_rigging_list_by_search_query,
    get_manual_list_by_search_query
)
from .mixins import ListViewMixin


class MainPageView(TemplateView):
    template_name = 'machinetools/main_page.html'


class StanokListView(ListViewMixin, ListView):
    model = Stanok
    template_name = 'machinetools/stanok_list.html'
    orders = ['power', 'rotation_frequency']

    def get_queryset_by_search_query(self, search_query):
        return get_stanok_list_by_search_query(search_query)


class InstrumentListView(ListViewMixin, ListView):
    model = Instrument
    template_name = 'machinetools/instrument_list.html'
    orders = ['workpiece_type', 'application_area']

    def get_queryset_by_search_query(self, search_query):
        return get_instrument_list_by_search_query(search_query)


class RiggingListView(ListViewMixin, ListView):
    model = Rigging
    template_name = 'machinetools/rigging_list.html'
    orders = ['rigging_type']

    def get_queryset_by_search_query(self, search_query):
        return get_rigging_list_by_search_query(search_query)


class ManualListView(ListViewMixin, ListView):
    model = Manual
    template_name = 'machinetools/manual_list.html'
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


class CalculatorView(TemplateView):
    template_name = 'machinetools/calculator.html'


class TurningCalculatorView(TemplateView):
    """Точение"""
    template_name = 'machinetools/calculators/turning.html'


class DrillingCalculatorView(TemplateView):
    """Сверление"""
    template_name = 'machinetools/calculators/drilling.html'


class BoringCalculatorView(TemplateView):
    """Растачивание"""
    template_name = 'machinetools/calculators/boring.html'


class MillingCalculatorView(TemplateView):
    """Фрезерование"""
    template_name = 'machinetools/calculators/milling.html'
