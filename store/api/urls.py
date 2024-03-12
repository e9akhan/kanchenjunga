"""
    Module name :- urls
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store.api.views import (
    EquipmentTypeList,
    EquipmentTypeDetail,
    EquipmentList,
    EquipmentDetail,
    AllocationList,
    AllocationDetail,
)

app_name = "store-apis"

urlpatterns = [
    path("equipment-types/", EquipmentTypeList.as_view(), name="equipment-type-list"),
    path(
        "equipment-type/<slug:slug>/",
        EquipmentTypeDetail.as_view(),
        name="equipment-type-detail",
    ),
    path("equipments/", EquipmentList.as_view(), name="equipment-list"),
    path("equipment/<slug:slug>/", EquipmentDetail.as_view(), name="equipment-detail"),
    path("allocations/", AllocationList.as_view(), name="allocation-list"),
    path(
        "allocation/<slug:slug>/", AllocationDetail.as_view(), name="allocation-detail"
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
