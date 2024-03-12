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
    lookup_field = "slug"


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
        search = self.request.GET.get("equipment_type", None)

        if search:
            return query.filter(
                equipment_type__in=EquipmentType.objects.filter(name__icontains=search)
            )
        return query


class EquipmentDetail(RetrieveUpdateDestroyAPIView):
    """
    Equipment Detail
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = "slug"


class AllocationList(ListCreateAPIView):
    """
    Allocation List.
    """

    serializer_class = AllocationSerializer

    def get_queryset(self):
        """
        get_queryset.
        """
        query = Allocation.objects.filter(returned=False)
        start_date = self.request.GET.get("start_date", None)
        end_date = self.request.GET.get("end_date", None)

        if start_date and end_date:
            return query.filter(
                allocated_date__gte=start_date, release_date__lte=end_date
            )

        if start_date:
            return query.filter(allocated_date__icontains=start_date)

        if end_date:
            return query.filter(release_date__icontains=end_date)


class AllocationDetail(RetrieveUpdateDestroyAPIView):
    """
    Allocation Detail
    """

    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
    lookup_field = "slug"
