"""
    Module name :- urls
"""

from django.urls import path
from store.views import (
    ListEquipmentType,
    CreateEquipmentType,
    UpdateEquipmentType,
    DeleteEquipmentType,
    CreateEquipment,
    UpdateEquipment,
    DeleteEquipment,
    DetailEquipment,
    ListParticularEquipments,
    CreateAllocation,
    SearchEquipment,
    SearchEquipmentType,
    SearchAssignedEquipment,
    get_ids
)

app_name = "store"

urlpatterns = [
    path("", ListEquipmentType.as_view(), name="equipment-types"),
    path(
        "add-equipment-type/", CreateEquipmentType.as_view(), name="add-equipment-type"
    ),
    path(
        "delete-equipment-type/<int:pk>/",
        DeleteEquipmentType.as_view(),
        name="delete-equipment-type",
    ),
    path("add-equipment/", CreateEquipment.as_view(), name="add-equipment"),
    path(
        "update-equipment/<int:pk>/", UpdateEquipment.as_view(), name="update-equipment"
    ),
    path(
        "delete-equipment/<int:pk>/", DeleteEquipment.as_view(), name="delete-equipment"
    ),
    path(
        'detail-equipment/<int:pk>/', DetailEquipment.as_view(), name='detail-equipment'
    ),
    path(
        "equipments/<str:equipment_type>/",
        ListParticularEquipments.as_view(),
        name="particular-equipments",
    ),
    path(
        "create-allocation/",
        CreateAllocation.as_view(),
        name='create-allocation'
    ),
    path("search-equipment/", SearchEquipment.as_view(), name="search-equipment"),
    path(
        "search-assigned-equipment/",
        SearchAssignedEquipment.as_view(),
        name="search-assigned-equipment",
    ),
    path(
        "search-equipment-type/",
        SearchEquipmentType.as_view(),
        name="search-equipment-type",
    ),
    path('get_ids/', get_ids, name='get_ids')
]
