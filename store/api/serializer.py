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
            "slug": {"write_only": True},
        }


class EquipmentSerializer(serializers.ModelSerializer):
    """
    Equipment Serializer.
    """

    equipment_type = serializers.CharField(max_length=100)

    class Meta:
        """
        Meta class
        """

        model = Equipment
        exclude = ("id", "slug")
        extra_kwargs = {"label": {"read_only": True}}

    def create(self, validated_data):
        """
        create method.
        """
        print("create")
        equipment_type_slug = validated_data.get("equipment_type", None)
        if equipment_type_slug:
            equipment_type = EquipmentType.objects.get(slug=equipment_type_slug)
            validated_data["equipment_type"] = equipment_type

        return Equipment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update method
        """
        equipment_type_slug = validated_data.get("equipment_type", None)

        if equipment_type_slug:
            equipment_type = Equipment.objects.get(slug=equipment_type_slug)
            validated_data["equipment_type"] = equipment_type

        return super().update(validated_data=validated_data, instance=instance)


class AllocationSerializer(serializers.ModelSerializer):
    """
    Allocation Serializer.
    """

    equipment_desc = serializers.SerializerMethodField()
    equipment = serializers.CharField(max_length=100)

    class Meta:
        """
        Meta class.
        """

        model = Allocation
        exclude = ("id", "slug", "release_date")
        extra_kwargs = {
            "equipment": {"write_only": True},
            "allocated_date": {"read_only": True},
        }

    def get_equipment_desc(self, obj):
        """
        get_equipment_desc method.
        """
        return EquipmentSerializer(obj.equipment).data

    def create(self, validated_data):
        """
        create method.
        """
        equipment_slug = validated_data.get("equipment", None)
        if equipment_slug:
            equipment = Equipment.objects.get(slug=equipment_slug)
            validated_data["equipment"] = equipment

        return Allocation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update method
        """
        equipment_slug = validated_data.get("equipment", None)

        if equipment_slug:
            equipment = Equipment.objects.get(slug=equipment_slug)
            validated_data["equipment"] = equipment

        return super().update(validated_data=validated_data, instance=instance)
