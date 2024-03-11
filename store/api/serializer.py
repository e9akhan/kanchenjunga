"""
    Module name :- serializer
"""

from rest_framework import serializers
from store.models import EquipmentType, Equipment, Allocation


class EquipmentTypeSerializer(serializers.ModelSerializer):
    """
    Equipment Type Serializer.
    """

    class Meta:
        """
        Meta class.
        """

        model = EquipmentType
        fields = ["id", "name", "get_remaining_equipments"]

        extra_kwargs = {
            "id": {"read_only": True},
            "get_remaining_equipments": {"read_only": True},
        }


class EquipmentSerializer(serializers.ModelSerializer):
    """
    Equipment Serializer.
    """

    class Meta:
        """
        Meta class
        """

        model = Equipment
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class AllocationSerializer(serializers.ModelSerializer):
    """
    Allocation Serializer.
    """

    equipment_desc = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class.
        """

        model = Allocation
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}, "equipment": {"write_only": True}}

    def get_equipment_desc(self, obj):
        return EquipmentSerializer(obj.equipment).data
