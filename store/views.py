"""
    Module name :- views
"""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from store.models import Department, Equipment, EquipmentType
from store.forms import EquipmentTypeForm, DepartmentForm, AddEquipmentForm, UpdateEquipmentForm

# Create your views here.
@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListDepartment(ListView):
    """
        List departments.
    """
    model = Department
    template_name = 'store/list_department.html'
    paginate_by = 8
    context_object_name = 'departments'
    
    def get_queryset(self):
        """
            Get queryset method.
        """
        return self.model.objects.all()[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateDepartment(CreateView):
    """
        Create department.
    """
    model = Department
    template_name = 'store/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('store:departments')

    def get_context_data(self, **kwargs):
        """
            Overridden get context data method.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Department'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateDepartment(UpdateView):
    """
        Update department.
    """
    model = Department
    template_name = 'store/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('store:departments')

    def get(self, request, *args, **kwargs):
        """
            Overridden get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'Department does not exists.')
            return redirect('store:departments')
        
        return super().get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        """
            Overridden get context data method.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Department'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class DeleteDepartment(DeleteView):
    """
        Delete department.
    """
    model = Department
    template_name = 'store/delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('store:departments')

    def get(self, request, *args, **kwargs):
        """
            Overridden get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'Department does not exists.')
            return redirect('store:departments')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
            Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Department'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListEquipmentType(ListView):
    """
        List equipment types.
    """
    model = EquipmentType
    template_name = 'store/list_equipment_type.html'
    context_object_name = 'equipment_types'
    paginate_by = 8


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateEquipmentType(CreateView):
    """
        Create equipment type.
    """
    model = EquipmentType
    template_name = 'store/form.html'
    form_class = EquipmentTypeForm
    success_url = reverse_lazy('store:equipment-types')

    def get_context_data(self, **kwargs):
        """
            Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Equipment Type'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateEquipmentType(UpdateView):
    """
        Update equipment type.
    """
    model = EquipmentType
    template_name = 'store/form.html'
    form_class = EquipmentTypeForm
    success_url = reverse_lazy('store:equipment-types')
    
    def get(self, request, *args, **kwargs):
        """
            Overridden get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'Equipment type does not exists.')
            return redirect('store:equipment-types')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
            Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Equipment Type'
        return context
    

@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class DeleteEquipmentType(DeleteView):
    """
        Delete equipment type.
    """
    model = EquipmentType
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:equipment-types')
    context_object_name = 'item'

    def get(self, request, *args, **kwargs):
        """
            Overridden get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'Equipment type does not exists.')
            return redirect('store:equipment-types')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
            Overriden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Equipment Type'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListParticularEquipments(ListView):
    """
        List particular equipments.
    """
    model = Equipment
    template_name = 'store/list_equipment.html'
    paginate_by = 8
    context_object_name = 'equipments'

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        return self.model.objects.filter(equipment_type__name = self.kwargs['equipment_type'], user=None)


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class ListEquipment(ListView):
    """
        List equipment.
    """
    model = Equipment
    template_name = 'store/list_assigned_equipment.html'
    paginate_by = 10
    context_object_name = 'equipments'

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        return self.model.objects.exclude(user = None)[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class CreateEquipment(CreateView):
    """
        Create equipment.
    """
    model = Equipment
    form_class = AddEquipmentForm
    template_name = 'store/form.html'
    success_url = reverse_lazy('store:equipment-types')

    def get_context_data(self, **kwargs):
        """
            Overridden get context data method.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Equipment'
        return context
    
    def form_valid(self, form):
        """
            Overridden form valid method.
        """
        quantity = form.cleaned_data['quantity']

        for _ in range(quantity-1):
            instance = self.model(
                equipment_type = form.cleaned_data['equipment_type']
            )
            instance.label = instance.set_label
            instance.save()

        return super().form_valid(form)
    

@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class UpdateEquipment(UpdateView):
    """
        Update equipment.
    """
    model = Equipment
    template_name = 'store/form.html'
    form_class = UpdateEquipmentForm
    success_url = reverse_lazy('store:equipments')

    def get_context_data(self, **kwargs):
        """
            Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Equipment'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class DeleteEquipment(DeleteView):
    """
        Delete equipment.
    """
    model = Equipment
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:equipments')

    def get_context_data(self, **kwargs):
        """
            Overridden get context data.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Equipment'
        return context


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class SearchEquipmentType(ListView):
    """
        Search equipment type.
    """
    model = EquipmentType
    template_name = 'store/list_equipment_type.html'
    context_object_name = 'equipment_types'
    paginate_by = 8

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        return self.model.objects.filter(name__icontains = self.request.GET['search'])


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class SearchDepartment(ListView):
    """
        Search Department.
    """
    model = Department
    template_name = 'store/list_department.html'
    context_object_name = 'departments'
    paginate_by = 8

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        return self.model.objects.filter(name__icontains = self.request.GET['search'])


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class SearchEquipment(ListView):
    """
        Search equipment.
    """
    model = Equipment
    template_name = 'store/list_equipment.html'
    context_object_name = 'equipments'
    paginate_by = 8

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        search = self.request.GET['search']
        return self.model.objects.filter(
            Q(label__icontains = search) | Q(department__name__icontains = search) |
            Q(equipment_type__name__icontains = search) |
            Q(functional = search), user = None
        )[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class SearchAssignedEquipment(ListView):
    """
        Search assigned equipment.
    """
    model = Equipment
    template_name = 'store/list_assigned_equipment.html'
    context_object_name = 'equipments'
    paginate_by = 8

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        search = self.request.GET['search']
        return self.model.objects.filter(
            Q(label__icontains = search) | Q(department__name__icontains = search) |
            Q(equipment_type__name__icontains = search) |
            Q(functional__icontains = search)
        ).exclude(user = None)[::-1]


@method_decorator(login_required(login_url='accounts:login'), name='dispatch')
class Alerts(ListView):
    """
        Alert.
    """
    model = EquipmentType
    template_name = 'store/alerts.html'
    context_object_name = 'alerts'
    paginate_by = 8

    def get_queryset(self):
        """
            Overridden get queryset method.
        """
        return [
            equipment_type
            for equipment_type in self.model.objects.all()
            if equipment_type.get_remaining_equipments <= 5
        ]