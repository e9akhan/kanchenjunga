"""
    Module name :- urls
"""

from django.urls import path
from store.views import (ListDepartment, CreateDepartment, UpdateDepartment, DeleteDepartment,
                         ListEquipmentType, CreateEquipmentType, UpdateEquipmentType, DeleteEquipmentType)

app_name = 'store'

urlpatterns = [
    path('departments/', ListDepartment.as_view(), name='departments'),
    path('add-department/', CreateDepartment.as_view(), name='add-department'),
    path('update-department/<int:pk>/', UpdateDepartment.as_view(), name='update-department'),
    path('delete-department/<int:pk>/', DeleteDepartment.as_view(), name='delete-department'),

    path('equipment-types/', ListEquipmentType.as_view(), name='equipment-types'),
    path('add-equipment-type/', CreateEquipmentType.as_view(), name='add-equipment-type'),
    path('update_equipment-type/<int:pk>/', UpdateEquipmentType.as_view(), name='update-equipment-type'),
    path('delete-equipment-type/<int:pk>/', DeleteEquipmentType.as_view(), name='delete-equipment-type')
]