from django.urls import path

from .views import IndexView, StanokListView, InstrumentListView, RiggingListView, StanokDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('stanok/<slug:pk>/', StanokDetailView.as_view(), name='stanok_detail'),
    path('stanok/', StanokListView.as_view(), name='stanok_list'),
    path('instrument/', InstrumentListView.as_view(), name='instrument_list'),
    path('rigging/', RiggingListView.as_view(), name='rigging_list'),
]
