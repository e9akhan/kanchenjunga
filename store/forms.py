"""
    Module name :- forms
"""

from django import forms
from django.contrib.auth.models import User
from store.models import Equipment, EquipmentType, Allocation


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


class EquipmentForm(forms.ModelForm):
    """
        Equipment Form.
    """

    equipment_type = forms.ModelChoiceField(queryset=EquipmentType.objects.all(), empty_label='Choose Equipment Type')

    class Meta:
        model = Equipment
        fields = ('serial_number', 'model_number', 'price', 'buy_date', 'brand')

        widgets = {
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
            ),
            'brand': forms.TextInput(
                attrs={'class': 'form-control'}
            )
        }

    equipment_type.widget.attrs.update({'class': 'form-select'})


class AddEquipmentForm(EquipmentForm):
    """
    Form for equipment
    """

    def save(self, commit=True):
        instance = super().save(commit=False)
        print(instance.equipment_type)
        instance.label = instance.set_label

        if commit:
            instance.save()
        return instance


class UpdateEquipmentForm(EquipmentForm):
    """
    Update form for equipment.
    """

    label = forms.CharField()
    functioal = forms.BooleanField()

    label.widget.attrs.update({'class': 'form-control', 'readonly': 'True'})


class AllocationForm(forms.ModelForm):
    """
        Allocation Form.
    """
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Choose User')

    class Meta:
        """
            Meta class.
        """
        model = Allocation
        fields = ('user', 'equipment')

        widgets = {
            'equipment': forms.TextInput(attrs={'class': 'form-select'})
        }

    user.widget.attrs.update({'class': 'form-select'})


class CreateAllocationForm(AllocationForm):
    """
        Create Allocation Form.
    """
    equipment_type = forms.ModelChoiceField(queryset=EquipmentType.objects.all(), empty_label='Choose Equipment')
    equipment_type.widget.attrs.update({'class': 'form-select'})


class UpdateAllocationForm(AllocationForm):
    """
        Update Allocation Form.
    """
    returned = forms.BooleanField()
