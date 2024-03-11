"""
    Module name :- urls
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from store.api.views import (
    EquipmentTypeList,
    EquipmentTypeDetail,
    EquipmentList,
    ParticularEquipmentList,
    EquipmentDetail,
    AllocationList,
    AllocationDetail,
)

app_name = "store-apis"

urlpatterns = [
    path("equipment-types/", EquipmentTypeList.as_view(), name="equipment-type-list"),
    path(
        "equipment-type/<int:pk>/",
        EquipmentTypeDetail.as_view(),
        name="equipment-type-detail",
    ),
    path("equipments/", EquipmentList.as_view(), name="equipment-list"),
    path(
        "equipments/<str:equipment_type>/",
        ParticularEquipmentList.as_view(),
        name="particular-equipment-list",
    ),
    path("equipment/<int:pk>/", EquipmentDetail.as_view(), name="equipment-detail"),
    path("allocations/", AllocationList.as_view(), name="allocation-list"),
    path("allocation/<int:pk>/", AllocationDetail.as_view(), name="allocation-detail"),
]


urlpatterns = format_suffix_patterns(urlpatterns)
