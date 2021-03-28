from django.urls import path
from .views import EntryList,EntryDetail

urlpatterns = [
    path('',EntryList.as_view(),name='entry_list'),
    path('<int:pk>',EntryDetail.as_view(),name='entry_detail')
]