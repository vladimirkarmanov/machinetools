from django.urls import path

from machinetools.views.ajax_view import calc_turning, calc_drilling, calc_boring, calc_milling

from machinetools.views.views import (
    MainPageView, StanokListView, InstrumentListView,
    RiggingListView, StanokDetailView, InstrumentDetailView,
    RiggingDetailView, ManualListView, CalculatorView,
    TurningCalculatorView, DrillingCalculatorView, BoringCalculatorView,
    MillingCalculatorView
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),

    path('stanok/<slug:pk>/', StanokDetailView.as_view(), name='stanok_detail'),
    path('stanok/', StanokListView.as_view(), name='stanok_list'),

    path('instrument/<slug:pk>/', InstrumentDetailView.as_view(), name='instrument_detail'),
    path('instrument/', InstrumentListView.as_view(), name='instrument_list'),

    path('rigging/<slug:pk>/', RiggingDetailView.as_view(), name='rigging_detail'),
    path('rigging/', RiggingListView.as_view(), name='rigging_list'),

    path('manual/', ManualListView.as_view(), name='manual_list'),

    path('calculator/', CalculatorView.as_view(), name='calculator'),
    path('calculator/turning/', TurningCalculatorView.as_view(), name='turning'),
    path('calculator/drilling/', DrillingCalculatorView.as_view(), name='drilling'),
    path('calculator/boring/', BoringCalculatorView.as_view(), name='boring'),
    path('calculator/milling/', MillingCalculatorView.as_view(), name='milling'),

    path('ajax/turning/', calc_turning, name='calc_turning'),
    path('ajax/drilling/', calc_drilling, name='calc_drilling'),
    path('ajax/boring/', calc_boring, name='calc_boring'),
    path('ajax/milling/', calc_milling, name='calc_milling'),
]
