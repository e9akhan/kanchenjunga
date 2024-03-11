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


class EquipmentList(ListCreateAPIView):
    """
    Equipment List.
    """

    queryset = Equipment.objects.filter(functional=True)
    serializer_class = EquipmentSerializer


class ParticularEquipmentList(ListCreateAPIView):
    """
    Equipment List.
    """

    serializer_class = EquipmentSerializer

    def get_queryset(self):
        """
        get_queryset method.
        """
        equipment_type = EquipmentType.objects.get(name=self.kwargs["equipment_type"])
        return Equipment.objects.filter(functional=True, equipment_type=equipment_type)


class EquipmentDetail(RetrieveUpdateDestroyAPIView):
    """
    Equipment Detail
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


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
