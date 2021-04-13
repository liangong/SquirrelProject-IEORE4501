from django.urls import path, re_path
from sightings.views import index, SightingDetail, AddSighting, stats

app_name = 'sightings'
urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<s_id>[0-9A-Z]+-[APM]{2}-[0-9]{4}-[0-9]{2})/$', SightingDetail.as_view(), name='detail'),
    path('add/', AddSighting.as_view(), name='add'),
    path('stats/', stats, name='stats'),
]