"""
    Module name :- views
"""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Equipment, EquipmentType, Allocation
from store.forms import (
    EquipmentTypeForm,
    AddEquipmentForm,
    UpdateEquipmentForm,
    CreateAllocationForm
)


# Create your views here.
@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListEquipmentType(ListView):
    """
    List equipment types.
    """

    model = EquipmentType
    template_name = "store/list_equipment_type.html"
    context_object_name = "equipment_types"


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateEquipmentType(CreateView):
    """
    Create equipment type.
    """

    model = EquipmentType
    template_name = "store/form.html"
    form_class = EquipmentTypeForm
    success_url = reverse_lazy("store:equipment-types")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Equipment Type"
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateEquipmentType(UpdateView):
    """
    Update equipment type.
    """

    model = EquipmentType
    template_name = "store/form.html"
    form_class = EquipmentTypeForm
    success_url = reverse_lazy("store:equipment-types")

    def get(self, request, *args, **kwargs):
        """
        Overridden get method.
        """
        try:
            self.get_object()
        except self.model.DoesNotExist:
            messages.info(request, "Equipment type does not exists.")
            return redirect("store:equipment-types")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Equipment Type"
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteEquipmentType(DeleteView):
    """
    Delete equipment type.
    """

    model = EquipmentType
    template_name = "store/delete.html"
    success_url = reverse_lazy("store:equipment-types")
    context_object_name = "item"

    def get(self, request, *args, **kwargs):
        """
        Overridden get method.
        """
        try:
            self.get_object()
        except self.model.DoesNotExist:
            messages.info(request, "Equipment type does not exists.")
            return redirect("store:equipment-types")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Overriden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Equipment Type"
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListParticularEquipments(ListView):
    """
    List particular equipments.
    """

    model = Equipment
    template_name = "store/list_equipment.html"
    paginate_by = 25
    context_object_name = "equipments"

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        return self.model.objects.filter(
            equipment_type__name=self.kwargs["equipment_type"]
        )[::-1]
    
    def get_context_data(self, **kwargs):
        """
            Get Context data.
        """
        context = super().get_context_data(**kwargs)
        context['total'] = len(self.get_queryset())
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateEquipment(CreateView):
    """
    Create equipment.
    """

    model = Equipment
    form_class = AddEquipmentForm
    template_name = "store/form.html"
    success_url = reverse_lazy("store:equipment-types")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data method.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Equipment"
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateEquipment(UpdateView):
    """
    Update equipment.
    """

    model = Equipment
    template_name = "store/form.html"
    form_class = UpdateEquipmentForm

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Equipment"
        return context
    
    def get_success_url(self):
        return reverse_lazy('store:particular-equipments', kwargs=self.kwargs['equipment_type'])


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteEquipment(DeleteView):
    """
    Delete equipment.
    """

    model = Equipment
    template_name = "store/delete.html"
    success_url = reverse_lazy("store:equipments")

    def get_context_data(self, **kwargs):
        """
        Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Equipment"
        return context


class DetailEquipment(LoginRequiredMixin, DetailView):
    """
        Detail Equipment.
    """
    login_url = reverse_lazy('accounts:login')
    model = Equipment
    template_name = 'store/detail.html'
    context_object_name = 'equipment'


class CreateAllocation(CreateView):
    """
        Create Allocation.
    """

    model = Allocation
    form_class = CreateAllocationForm
    template_name = 'store/create_allocation.html'
    success_url = reverse_lazy('store:create-allocation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Allocation'
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class SearchEquipmentType(ListView):
    """
    Search equipment type.
    """

    model = EquipmentType
    template_name = "store/list_equipment_type.html"
    context_object_name = "equipment_types"
    paginate_by = 8

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        return self.model.objects.filter(name__icontains=self.request.GET["search"])


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class SearchEquipment(ListView):
    """
    Search equipment.
    """

    model = Equipment
    template_name = "store/list_equipment.html"
    context_object_name = "equipments"
    paginate_by = 8

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        search = self.request.GET["search"]
        return self.model.objects.filter(
            Q(label__icontains=search)
            | Q(equipment_type__name__icontains=search)
            | Q(functional__icontains=search),
        )[::-1]


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class SearchAssignedEquipment(ListView):
    """
    Search assigned equipment.
    """

    model = Equipment
    template_name = "store/list_assigned_equipment.html"
    context_object_name = "equipments"
    paginate_by = 8

    def get_queryset(self):
        """
        Overridden get queryset method.
        """
        search = self.request.GET["search"]
        return self.model.objects.filter(
            Q(label__icontains=search)
            | Q(equipment_type__name__icontains=search)
            | Q(functional__icontains=search)
        )[::-1]


def get_ids(request):
    return EquipmentType.objects.get(id = request.GET['equipment_type']).get_remaining_equipments