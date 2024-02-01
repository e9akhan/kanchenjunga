"""
    Module name :- forms
"""

from django import forms
from store.models import Department, Equipment, EquipmentType


class DepartmentForm(forms.ModelForm):
    """
        Form for department.
    """

    class Meta:
        """
            Meta class for department form.
        """

        model = Department
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class EquipmentTypeForm(forms.ModelForm):
    """
        Form for equipment type.
    """

    class Meta:
        """
            Meta class for equipment type form.
        """

        model = EquipmentType
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class EquipmentForm(forms.Form):
    """
        Form for equipment
    """

    equipment_type = forms.ModelChoiceField(queryset=EquipmentType.objects.all(), empty_label='Add Equipment Type')
    quantity = forms.IntegerField()

    equipment_type.widget.attrs.update({'class': 'form-select'})
    quantity.widget.attrs.update({'class': 'form-control', 'placeholder': 0})