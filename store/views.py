from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from django.db.models import Q
from store.models import Department, Equipment, EquipmentType
from store.forms import EquipmentTypeForm, DepartmentForm, AddEquipmentForm, UpdateEquipmentForm

# Create your views here.
class ListDepartment(ListView):
    model = Department
    template_name = 'store/list_department.html'
    paginate_by = 10
    context_object_name = 'departments'
    
    def get_queryset(self):
        return self.model.objects.all()[::-1]


class CreateDepartment(CreateView):
    model = Department
    template_name = 'store/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('store:departments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Department'
        return context


class UpdateDepartment(UpdateView):
    model = Department
    template_name = 'store/form.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('store:departments')

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, 'Department does not exists.')
            return redirect('store:departments')
        
        return super().get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Department'
        return context


class DeleteDepartment(DeleteView):
    model = Department
    template_name = 'store/delete.html'
    context_object_name = 'item'
    success_url = reverse_lazy('store:departments')

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, 'Department does not exists.')
            return redirect('store:departments')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Department'
        return context


class ListEquipmentType(ListView):
    model = EquipmentType
    template_name = 'store/list_equipment_type.html'
    context_object_name = 'equipment_types'
    paginate_by = 10


class CreateEquipmentType(CreateView):
    model = EquipmentType
    template_name = 'store/form.html'
    form_class = EquipmentTypeForm
    success_url = reverse_lazy('store:equipment-types')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Equipment Type'
        return context


class UpdateEquipmentType(UpdateView):
    model = EquipmentType
    template_name = 'store/form.html'
    form_class = EquipmentTypeForm
    success_url = reverse_lazy('store:equipment-types')
    
    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, 'Equipment type does not exists.')
            return redirect('store:equipment-types')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Equipment Type'
        return context
    

class DeleteEquipmentType(DeleteView):
    model = EquipmentType
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:equipment-types')
    context_object_name = 'item'

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except:
            messages.info(request, 'Equipment type does not exists.')
            return redirect('store:equipment-types')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Equipment Type'
        return context


class ListParticularEquipments(ListView):
    model = Equipment
    template_name = 'store/list_equipment.html'
    paginate_by = 10
    context_object_name = 'equipments'

    def get_queryset(self):
        return self.model.objects.filter(equipment_type__name = self.kwargs['equipment_type'], user=None)


class ListEquipment(ListView):
    model = Equipment
    template_name = 'store/list_equipment.html'
    paginate_by = 10
    context_object_name = 'equipments'

    def get_queryset(self):
        return self.model.objects.exclude(user = None)


class CreateEquipment(CreateView):
    model = Equipment
    form_class = AddEquipmentForm
    template_name = 'store/form.html'
    success_url = reverse_lazy('store:equipments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Equipment'
        return context
    
    def form_valid(self, form):
        quantity = form.cleaned_data['quantity']

        for _ in range(quantity-1):
            instance = self.model(
                equipment_type = form.cleaned_data['equipment_type']
            )
            instance.label = instance.set_label
            instance.save()

        return super().form_valid(form)
    

class UpdateEquipment(UpdateView):
    model = Equipment
    template_name = 'store/form.html'
    form_class = UpdateEquipmentForm
    success_url = reverse_lazy('store:equipments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Equipment'
        return context


class DeleteEquipment(DeleteView):
    model = Equipment
    template_name = 'store/delete.html'
    success_url = reverse_lazy('store:equipments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Equipment'
        return context


class SearchEquipmentType(ListView):
    model = EquipmentType
    template_name = 'store/list_equipment_type.html'
    context_object_name = 'equipment_types'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(name__icontains = self.request.GET['search'])


class SearchDepartment(ListView):
    model = Department
    template_name = 'store/list_department.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(name__icontains = self.request.GET['search'])


class SearchEquipment(ListView):
    model = Equipment
    template_name = 'store/list_equipment.html'
    context_object_name = 'equipments'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET['search']
        return self.model.objects.filter(
            Q(label__icontains = search) | Q(department__name__icontains = search) |
            Q(equipment_type__name__icontains = search) |
            Q(functional__icontains = search)
        )[::-1]