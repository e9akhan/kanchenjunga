"""
    Module name :- forms
"""

from django import forms
from django.contrib.auth.models import User
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
        fields = ("name",)

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


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
        fields = ("label", "user", "department", "functional")

        widgets = {
            "label": forms.TextInput(
                attrs={"class": "form-control", "readonly": "True"}
            ),
        }

    user = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Choose User", required=False
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Choose Department",
        required=False,
    )

    user.widget.attrs.update({"class": "form-select"})
    department.widget.attrs.update({"class": "form-select"})
