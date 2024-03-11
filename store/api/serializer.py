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
        fields = ["name", "get_remaining_equipments"]

        extra_kwargs = {
            "get_remaining_equipments": {"read_only": True},
            'slug': {'write_only': True}
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
        exclude = ('id',)
        extra_kwargs = {
            'slug': {'write_only': True}
        }


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
        exclude = ('id',)
        extra_kwargs = {"equipment": {"write_only": True}}

    def get_equipment_desc(self, obj):
        """
            get_equipment_desc method.
        """
        return EquipmentSerializer(obj.equipment).data
