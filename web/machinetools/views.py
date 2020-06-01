from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView, View

from .models import Stanok, Instrument, Rigging, Manual
from .services import (
    get_stanok_list_by_search_query,
    get_instrument_list_by_search_query,
    get_rigging_list_by_search_query,
    get_manual_list_by_search_query
)
from .utils import get_objects_page


class IndexView(TemplateView):
    template_name = 'machinetools/index.html'


class StanokListView(View):
    model = Stanok
    template_name = 'machinetools/stanok_list.html'

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            stanok_list = get_stanok_list_by_search_query(search_query)
        else:
            stanok_list = self.model.objects.order_by('group__name')

        page_number = request.GET.get('page', 1)
        page = get_objects_page(stanok_list, 9, page_number)

        return render(request, self.template_name, {'search_value': search_query, 'page': page})


class StanokDetailView(DetailView):
    model = Stanok
    template_name = 'machinetools/stanok_detail.html'


class InstrumentListView(View):
    model = Instrument
    template_name = 'machinetools/instrument_list.html'

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            instrument_list = get_instrument_list_by_search_query(search_query)
        else:
            instrument_list = self.model.objects.order_by('name')

        page_number = request.GET.get('page', 1)
        page = get_objects_page(instrument_list, 9, page_number)

        return render(request, self.template_name, {'search_value': search_query, 'page': page})


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = 'machinetools/instrument_detail.html'


class RiggingListView(View):
    model = Rigging
    template_name = 'machinetools/rigging_list.html'

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            rigging_list = get_rigging_list_by_search_query(search_query)
        else:
            rigging_list = self.model.objects.order_by('rigging_type__name')

        page_number = request.GET.get('page', 1)
        page = get_objects_page(rigging_list, 9, page_number)

        return render(request, self.template_name, {'search_value': search_query, 'page': page})


class RiggingDetailView(DetailView):
    model = Rigging
    template_name = 'machinetools/rigging_detail.html'


class ManualListView(View):
    model = Manual
    template_name = 'machinetools/manual_list.html'

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            manual_list = get_manual_list_by_search_query(search_query)
        else:
            manual_list = self.model.objects.order_by('name')

        page_number = request.GET.get('page', 1)
        page = get_objects_page(manual_list, 9, page_number)

        return render(request, self.template_name, {'search_value': search_query, 'page': page})
