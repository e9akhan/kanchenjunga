"""
    Module name :- forms
"""

from django import forms
from django.contrib.auth.models import User
from store.models import Equipment, EquipmentType


# class DepartmentForm(forms.ModelForm):
#     """
#     Form for department.
#     """

#     class Meta:
#         """
#         Meta class for department form.
#         """

#         model = Department
#         fields = ("name",)

#         widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class EquipmentTypeForm(forms.ModelForm):
    """
    Form for equipment type.
    """

    class Meta:
        """
        Meta class for equipment type form.
        """

        model = EquipmentType
        fields = ("name",)

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class AddEquipmentForm(forms.ModelForm):
    """
    Form for equipment
    """

    equipment_type = forms.ModelChoiceField(
        queryset=EquipmentType.objects.all(), empty_label="Add Equipment Type"
    )
    quantity = forms.IntegerField()

    equipment_type.widget.attrs.update({"class": "form-select"})
    quantity.widget.attrs.update({"class": "form-control", "placeholder": 0})

    class Meta:
        """
        Meta class.
        """

        model = Equipment
        fields = ("equipment_type",)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.label = instance.set_label

        if commit:
            instance.save()
        return instance


class UpdateEquipmentForm(forms.ModelForm):
    """
    Update form for equipment.
    """

    class Meta:
        """
        Meta class for update equipment form.
        """

        model = Equipment
        fields = ("label", 'serial_number', "model_number", "price", "buy_date", "functional")

        widgets = {
            "label": forms.TextInput(
                attrs={"class": "form-control", "readonly": "True"}
            ),
            "serial_number": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "model_number": forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            "price": forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'buy_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            )
        }
