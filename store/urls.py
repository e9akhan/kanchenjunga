"""
    Module name :- urls
"""

from django.urls import path
from store.views import index

app_name = 'store'

urlpatterns = [
    path('store/', index, name='index')
]