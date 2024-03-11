"""
    Module name :- views
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from store.models import EquipmentType, Equipment, Allocation
from store.api.serializer import (
    EquipmentTypeSerializer,
    EquipmentSerializer,
    AllocationSerializer,
)


class EquipmentTypeList(ListCreateAPIView):
    """
    Equipment Type List.
    """

    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentTypeDetail(RetrieveUpdateDestroyAPIView):
    """
    Equipment Type Detail.
    """

    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    lookup_field = 'slug'


class EquipmentList(ListCreateAPIView):
    """
    Equipment List.
    """

    serializer_class = EquipmentSerializer

    def get_queryset(self):
        """
            get_queryset.
        """
        query = Equipment.objects.filter(functional=True)
        search = self.request.GET.get('equipment_type', None)

        if search:
            return query.filter(equipment_type=EquipmentType.objects.get(name=search))
        return query


class EquipmentDetail(RetrieveUpdateDestroyAPIView):
    """
    Equipment Detail
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'slug'


class AllocationList(ListCreateAPIView):
    """
    Allocation List.
    """

    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


class AllocationDetail(RetrieveUpdateDestroyAPIView):
    """
    Allocation Detail
    """

    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
