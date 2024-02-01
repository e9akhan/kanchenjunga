from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib import messages
from store.models import Department, Equipment, EquipmentType
from store.forms import EquipmentForm, EquipmentTypeForm, DepartmentForm

# Create your views here.
def index(request):
    return render(request, 'store/base.html')


class ListDepartment(ListView):
    model = Department
    template_name = 'store/list_department.html'
    paginate_by = 8
    context_object_name = 'departments'


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
    paginate_by = 8


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
