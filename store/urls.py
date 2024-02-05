"""
    Module name :- urls
"""

from django.urls import path
from store.views import (
    ListDepartment,
    CreateDepartment,
    UpdateDepartment,
    DeleteDepartment,
    ListEquipmentType,
    CreateEquipmentType,
    UpdateEquipmentType,
    DeleteEquipmentType,
    ListEquipment,
    CreateEquipment,
    UpdateEquipment,
    DeleteEquipment,
    ListParticularEquipments,
    SearchDepartment,
    SearchEquipment,
    SearchEquipmentType,
    SearchAssignedEquipment,
    Alerts,
)

app_name = "store"

urlpatterns = [
    path("departments/", ListDepartment.as_view(), name="departments"),
    path("add-department/", CreateDepartment.as_view(), name="add-department"),
    path(
        "update-department/<int:pk>/",
        UpdateDepartment.as_view(),
        name="update-department",
    ),
    path(
        "delete-department/<int:pk>/",
        DeleteDepartment.as_view(),
        name="delete-department",
    ),
    path("", ListEquipmentType.as_view(), name="equipment-types"),
    path(
        "add-equipment-type/", CreateEquipmentType.as_view(), name="add-equipment-type"
    ),
    path(
        "update_equipment-type/<int:pk>/",
        UpdateEquipmentType.as_view(),
        name="update-equipment-type",
    ),
    path(
        "delete-equipment-type/<int:pk>/",
        DeleteEquipmentType.as_view(),
        name="delete-equipment-type",
    ),
    path("equipments/", ListEquipment.as_view(), name="equipments"),
    path("add-equipment/", CreateEquipment.as_view(), name="add-equipment"),
    path(
        "update-equipment/<int:pk>/", UpdateEquipment.as_view(), name="update-equipment"
    ),
    path(
        "delete-equipment/<int:pk>/", DeleteEquipment.as_view(), name="delete-equipment"
    ),
    path(
        "equipments/<str:equipment_type>/",
        ListParticularEquipments.as_view(),
        name="particular-equipments",
    ),
    path("search-equipment/", SearchEquipment.as_view(), name="search-equipment"),
    path(
        "search-assigned-equipment/",
        SearchAssignedEquipment.as_view(),
        name="search-assigned-equipment",
    ),
    path("search-department/", SearchDepartment.as_view(), name="search-department"),
    path(
        "search-equipment-type/",
        SearchEquipmentType.as_view(),
        name="search-equipment-type",
    ),
    path("alerts/", Alerts.as_view(), name="alerts"),
]
